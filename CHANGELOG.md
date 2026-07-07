# observability Changelog

All notable changes to the eCOS observability stack (Langfuse + Webhook Bridge) are documented in this file.

## [Unreleased]

### Added
- **README.md**: complete project overview with service table, configuration, and deployment instructions.
- **CAPABILITY-MAP.md**: observability capability map.
- Langfuse self-hosted LLM observability platform (trace, evaluate, prompt management).
- Webhook Bridge to poll Langfuse events and forward to OMO governance webhooks.
- Postgres persistence layer for Langfuse.

### Security
- Secrets must be kept in `.env` files only; never commit real credentials.
- Ports are registered in the workspace `protocols/port-registry.yaml`.

## Notes

This project follows the workspace release cadence. For cross-project changes that affect observability, also update the workspace root [`CHANGELOG.md`](../../CHANGELOG.md).
