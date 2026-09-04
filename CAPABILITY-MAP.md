---
type: ssot
owner: governance-team
last_updated: 2026-09-03
---

# observability 能力地图

> Langfuse + Webhook Bridge · LLM 可观测性部署面 · X 层横切

---

## 一、架构定位

```
┌─────────────────────────────────────────────────────────────┐
│              observability — 可观测性部署面                     │
├─────────────────────────────────────────────────────────────┤
│  Langfuse Server  │  Webhook Bridge  │  Postgres  │  OTEL    │
│  LLM 追踪/评估     │  事件转发→OMO     │  持久化    │  OpenTelemetry │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、核心功能

| 功能 | 说明 |
|------|------|
| LLM 追踪 | Langfuse trace / span / generation 追踪 |
| 事件转发 | webhook-bridge 轮询 Langfuse 事件 → OMO governance webhook |
| 持久化 | Postgres 15 数据存储 |
| OTEL 集成 | kairon OTLP tracing 接入 |

---

## 三、服务结构

| 服务 | 镜像 | 用途 |
|------|------|------|
| langfuse-server | `ghcr.io/langfuse/langfuse:2` | Langfuse Web UI + API |
| webhook-bridge | `python:3.12-slim` | 事件转发到 OMO |
| db | `postgres:15` | 持久化层 |

---

## 四、部署

```bash
docker compose up -d      # 启动所有服务
docker compose ps         # 查看状态
docker compose config -q  # 验证配置
```

端口: 见 `protocols/port-registry.yaml`
环境变量: 见根 `.env.example`

---

## 五、下游影响

- kairon: OTLP tracing 发送到 Langfuse
- OMO: webhook-bridge 转发事件到 governance webhook

---

*项目元数据: [`../../docs/project-registry.yaml`](../../docs/project-registry.yaml)*
