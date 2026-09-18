---
type: derived
source: projects/observability
owner: governance-team
last_updated: 2026-09-03
last-reviewed: 2026-09-18

---

# observability

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributing](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Security](https://img.shields.io/badge/security-policy-blue.svg)](SECURITY.md)
[![Docker](https://img.shields.io/badge/Docker-supported-2496ED.svg)](https://www.docker.com/)

> Langfuse + Webhook Bridge for eCOS observability.

## What This Project Does

- **Langfuse**: Self-hosted LLM observability platform (trace, evaluate, prompt management).
- **Webhook Bridge**: Polls Langfuse events and forwards to OMO governance webhooks.
- **Postgres**: Persistence layer for Langfuse.

## Quick Start

```bash
# Prepare local credentials (fill in real values for shared or production use)
cp .env.example .env

# Start all services
docker compose --env-file .env up -d

# Check status
docker compose --env-file .env ps

# View logs
docker compose --env-file .env logs -f

# Verify config
docker compose --env-file .env config -q
```

## Services

| Service | Image | Purpose |
|---------|-------|---------|
| langfuse-server | ghcr.io/langfuse/langfuse:2 | Langfuse web UI and API |
| webhook-bridge | python:3.12-slim | Event forwarding to OMO |
| db | postgres:15 | Persistence |

## Configuration

- Ports: see `protocols/port-registry.yaml`
- Secrets: use `.env` file (never commit real secrets)
- Environment variables: see root `.env.example`

## Related Docs

- [AGENTS.md](AGENTS.md) — Developer guide
- [ARCHITECTURE.md](ARCHITECTURE.md) — Project architecture
- [BOUNDARY.md](BOUNDARY.md) — System boundary
- [CALLCHAIN.md](CALLCHAIN.md) — Call chain
- [Workspace Architecture](../../ARCHITECTURE.md)
- [Project Registry](../../docs/project-registry.yaml)
## Project Governance

- [Contributing](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)
- [Code of Conduct](CODE_OF_CONDUCT.md)

---

## 项目状态 (动态数据)

| 指标 | 权威读源 | 说明 |
|------|----------|------|
| 版本 | `pyproject.toml` → `[project.version]` | 以 pyproject.toml 为准 |
| 测试数 | `pytest --collect-only -q` | 动态计数 |
| 代码行数 | `find src -name "*.py" \| wc -l` | 以实际文件为准 |
| 源文件数 | `find src -name "*.py" \| wc -l` | 以实际文件为准 |
| 测试文件数 | `find tests -name "*.py" \| wc -l` | 以实际文件为准 |

> **doc-ssot 契约**: 上表中的所有数字均为易变事实, 不在本文件硬编码. 运行权威读源命令获取实时值.
> 模板: `.omo/standards/readme-template.md` | 检测: `bin/gac/check-readme-hardcoded.py`

