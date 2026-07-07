# observability

> Langfuse + Webhook Bridge for eCOS observability.

## What This Project Does

- **Langfuse**: Self-hosted LLM observability platform (trace, evaluate, prompt management).
- **Webhook Bridge**: Polls Langfuse events and forwards to OMO governance webhooks.
- **Postgres**: Persistence layer for Langfuse.

## Quick Start

```bash
# Start all services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f

# Verify config
docker compose config -q
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
