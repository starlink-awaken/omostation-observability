---
type: ssot
owner: governance-team
last_updated: 2026-09-03
---

# observability API / Usage Reference

> Quick reference for using **observability** programmatically and from the command line.

## Command Line

- `docker compose up -d` — start stack
- `docker compose ps` — status
- `docker compose logs -f` — logs

## Programmatic API

Use Langfuse API and webhook bridge endpoints; see environment templates.

## Configuration

- Stack: docker
- Dependencies: see [`../pyproject.toml`](../pyproject.toml) (Python) or [`../package.json`](../package.json) (TypeScript).
- Environment variables and ports: see workspace `protocols/port-registry.yaml` and root `.env.example`.

## Tests

See [`../README.md`](../README.md) for the test command.
