---
type: ssot
owner: governance-team
last_updated: 2026-09-03
last-reviewed: 2026-09-18

---

# CLAUDE.md — observability AI Context

> Session loader for AI work inside `observability`.
> Keep durable engineering rules in [`AGENTS.md`](AGENTS.md) and volatile facts in SSOT files.

## Load First

1. [`AGENTS.md`](AGENTS.md)
2. The deployment files directly related to the task
3. Workspace context in [`../../CLAUDE.md`](../../CLAUDE.md) when the task crosses project boundaries

## Project Role

- Layer: X
- Responsibility: Langfuse / OTEL 可观测性部署面
- Stack: Docker / compose

## Commands

```bash
docker compose up -d
docker compose ps
docker compose logs -f
```

## Safe Editing Rules

- 服务端口和外部访问地址以端口注册表和部署环境为准。
- 不要提交真实密钥或本地 .env。
- Do not commit, push, reset, or bump submodule pointers unless the user explicitly asks.
- Preserve unrelated dirty changes in this repository.
- Keep Markdown pointed at SSOT files instead of copying generated facts.

## Closeout

```bash
git status --short
uv run --with "pyyaml" python "../../bin/ssot/doc-ssot-lint.py" --json
```

Report the checks you actually ran and any pre-existing dirty state that remains.
