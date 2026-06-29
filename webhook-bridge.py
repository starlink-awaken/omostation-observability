"""Langfuse alert → omo event bridge.

Polls Langfuse API for new alerts/observations and forwards them as omo events.
Runs as a sidecar container alongside Langfuse.

Non-blocking: if omo is unavailable, alerts are queued locally and retried.
"""

from __future__ import annotations

import json
import os
import time
import urllib.request
from pathlib import Path

LANGFUSE_URL = os.environ.get("LANGFUSE_URL", "http://localhost:3000")
LANGFUSE_API_KEY = os.environ.get("LANGFUSE_API_KEY", "")
OMO_WEBHOOK_URL = os.environ.get("OMO_WEBHOOK_URL", "http://localhost:9100/webhook")
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "60"))
QUEUE_FILE = Path("/tmp/omo_alert_queue.jsonl")


def fetch_langfuse_alerts(since_ts: int) -> list[dict]:
    """Fetch alerts from Langfuse API since given timestamp."""
    if not LANGFUSE_API_KEY:
        return []
    try:
        url = f"{LANGFUSE_URL}/api/public/observations?fromTimestamp={since_ts}"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {LANGFUSE_API_KEY}"})
        with urllib.request.urlopen(req, timeout=5.0) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("data", [])
    except Exception:  # noqa: BLE001  # non-blocking poll
        return []


def forward_to_omo(alert: dict) -> bool:
    """Forward an alert to omo webhook. Returns True on success."""
    payload = {
        "source": "observability",
        "event": "langfuse_alert",
        "data": alert,
        "timestamp": int(time.time()),
    }
    try:
        req = urllib.request.Request(
            OMO_WEBHOOK_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(req, timeout=3.0)
        return True
    except Exception:  # noqa: BLE001  # non-blocking, queue for retry
        # Queue failed alert for retry
        with open(QUEUE_FILE, "a") as f:
            f.write(json.dumps(payload) + "\n")
        return False


def replay_queued() -> int:
    """Replay queued alerts. Returns count of successfully sent."""
    if not QUEUE_FILE.exists():
        return 0
    lines = QUEUE_FILE.read_text().strip().split("\n") if QUEUE_FILE.read_text().strip() else []
    remaining = []
    sent = 0
    for line in lines:
        payload = json.loads(line)
        try:
            req = urllib.request.Request(
                OMO_WEBHOOK_URL,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            urllib.request.urlopen(req, timeout=3.0)
            sent += 1
        except Exception:  # noqa: BLE001
            remaining.append(line)
    QUEUE_FILE.write_text("\n".join(remaining) + ("\n" if remaining else ""))
    return sent


def main():
    """Main poll loop."""
    print(f"[webhook-bridge] Langfuse={LANGFUSE_URL} → omo={OMO_WEBHOOK_URL} interval={POLL_INTERVAL}s")
    last_ts = int(time.time())
    while True:
        replay_queued()
        alerts = fetch_langfuse_alerts(last_ts)
        for alert in alerts:
            forward_to_omo(alert)
        if alerts:
            last_ts = max(a.get("createdAt", last_ts) for a in alerts if isinstance(a.get("createdAt"), int))
            print(f"[webhook-bridge] Forwarded {len(alerts)} alerts")
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
