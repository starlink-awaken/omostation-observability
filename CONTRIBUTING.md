---
type: ssot
owner: governance-team
last_updated: 2026-09-03
---

# Contributing to observability

> Langfuse + Webhook Bridge for eCOS observability
> Langfuse + Webhook Bridge 可观测性栈

Thank you for considering a contribution! This guide covers the development workflow, commit conventions, and review process for **observability**.

## Development Environment

- **Stack**: Docker (Langfuse, Postgres, Python)
- **Python requirement**: see [`pyproject.toml`](pyproject.toml) (if applicable)

## Quick Start

```bash
# Install dependencies
docker compose pull

# Run tests
docker compose config -q

# Run lint
# No lint target configured
```

## Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat(scope):` — New feature
- `fix(scope):` — Bug fix
- `refactor(scope):` — Code refactoring
- `docs(scope):` — Documentation
- `test(scope):` — Tests
- `chore(scope):` — Maintenance

## Code Standards

- Keep changes focused and scoped to one concern per PR.
- Add or update tests for new behavior.
- Ensure the lint/test commands above pass before requesting review.

## Project-Specific Notes

- Never commit real secrets; use `.env` files derived from root `.env.example`.
- Validate `docker compose config -q` after changing compose files or environment templates.

## Pull Request Process

1. Create a feature branch from `main`.
2. Make changes following the conventions above.
3. Run the project's test and lint commands.
4. Submit a PR with a clear description of the change and its motivation.

## Getting Help

- See [`AGENTS.md`](AGENTS.md) for AI-agent developer rules.
- See [`CLAUDE.md`](CLAUDE.md) for session startup context.
- Workspace architecture: [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md)
