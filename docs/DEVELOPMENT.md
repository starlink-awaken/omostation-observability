---
type: ssot
owner: governance-team
last_updated: 2026-09-03
---

# Development Guide

Thank you for contributing to this project. This guide covers how to set up a local development environment, run tests, and submit changes.

## Development Environment

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Clone the workspace recursively:
   ```bash
   git clone --recursive https://github.com/starlink-awaken/omostation.git
   cd omostation/projects/observability
   ```
3. Build and start services:
   ```bash
   docker compose up -d
   ```

## Project Structure

- `docker-compose.yml` — Langfuse + Postgres + OMO webhook-bridge 编排
- `webhook-bridge.py` — 将 Langfuse 事件转发到 OMO governance webhook 的 sidecar 脚本
- `.env.example` — 环境变量模板
- `docs/` — Documentation
- `README.md` — Project overview

> 注：本项目是部署/集成面，以 Docker Compose 和单一桥接脚本为主，因此不存在传统意义上的 `src/` 源码目录与 `tests/` 单元测试目录。

## Coding Conventions

- Follow the existing style in the codebase.
- Add tests for new functionality.
- Keep documentation in sync with code changes.

## Submitting Changes

1. Open an issue to discuss large changes.
2. Create a feature branch from `main`.
3. Make focused commits with clear messages.
4. Ensure tests pass locally.
5. Open a pull request and fill out the template.

## Releasing

See [`RELEASE.md`](RELEASE.md) for the release checklist.
