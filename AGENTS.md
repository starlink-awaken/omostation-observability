# AGENTS.md — observability (Langfuse 可观测性部署)

> X 层 (横切) · Docker Compose 部署
> 状态: 🟢 Active
> 最后更新: 2026-06-24

## Project Identity

observability 是 eCOS v5 系统的**可观测性基础设施**，基于 Langfuse (LLM 应用专用 observability 平台) 部署。

- **不是 Python 包**: 仅 docker-compose.yml + 配置
- **不参与 runtime 链路**: 独立部署，通过 HTTP 接收 trace 数据
- **5+4+1+1 架构位置**: X 横切层 (与 aetherforge/model-driven/bus-foundation 并列)

## 部署架构

```yaml
# docker-compose.yml
services:
  langfuse-web:        # Langfuse Web UI (port 3000)
  langfuse-worker:     # 后台处理 worker
  postgres:            # 元数据存储
  clickhouse:          # trace 存储
  redis:               # 缓存
  minio:               # 对象存储
```

## 端口

| 端口 | 服务 | 说明 |
|------|------|------|
| 3000 | langfuse-web | Web UI |
| 5433 | postgres | 元数据 (宿主机映射,避免与本地 postgres 5432 冲突) |
| 9000 | minio | 对象存储 (内部) |

详见 `protocols/port-registry.yaml`。

## 启动

```bash
cd projects/observability
docker compose up -d
# 访问 http://localhost:3000
```

## 与 eCOS 集成

所有 L1/L2 项目 (kairon/gbrain/aetherforge/omo) 通过 Langfuse SDK 上报 trace:
- `OMITL_TRACES_EXPORTER=otlp` (环境变量)
- `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:3000/api/public/otel`

## 治理合规

- ✅ ARCHITECTURE.md / BOUNDARY.md / CALLCHAIN.md 完整
- ⚠️ 无 pyproject.toml (Docker 项目，不需要)
- ⚠️ 无 tests/ 目录 (Docker 部署，无单元测试)
- ⚠️ 无 Python 源码 (架构上不需要)

## 关联

- `protocols/port-registry.yaml` — 端口注册
- `.omo/_truth/registry/mutation-surfaces.yaml` — 治理面写入入口
- `AGENTS.md` (根) — 工作区指南
