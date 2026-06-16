# observability — System Boundary

> 本文档描述 observability 与 eCOS 系统其他部分的边界：暴露的接口、依赖的上游、影响的下游。
>
> 架构演进对比参见：[`docs/ARCHITECTURE-EVOLUTION.md`](../docs/ARCHITECTURE-EVOLUTION.md)

---

## 1. 暴露接口

### BOS URI



### 入口

- **Docker**: `docker compose up` Langfuse Web :3000, Postgres :5432

## 2. 上游依赖



## 3. 下游影响

- kairon (OTLP tracing)

## 4. 配置 / SSOT

- 项目源码：`projects/observability/`
- 入口定义：`projects/observability/pyproject.toml` 或 `package.json`
- 测试：`cd projects/observability && docker compose up -d`
