# Observability

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributing](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Security](https://img.shields.io/badge/security-policy-blue.svg)](SECURITY.md)
[![Docker](https://img.shields.io/badge/Docker-supported-2496ED.svg)](https://www.docker.com/)

## 项目定位

Langfuse 可观测性（所属层级：X；技术栈：Docker）。

## 安装

```bash
# Clone the workspace recursively
git clone --recursive https://github.com/starlink-awaken/omostation.git
cd omostation/projects/observability

# Pull and start services
docker compose pull
docker compose up -d
```

Requires Docker and Docker Compose.

## 快速开始

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

## 文档

- 英文 README: [`README.md`](README.md)
- 贡献指南: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- 安全策略: [`SECURITY.md`](SECURITY.md)
- 更新日志: [`CHANGELOG.md`](CHANGELOG.md)
- 行为准则: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- 贡献者名单: [`CONTRIBUTORS.md`](CONTRIBUTORS.md)

## 获取帮助

- [FAQ](docs/FAQ.md)
- [故障排查](docs/TROUBLESHOOTING.md)
- [API / 使用参考](docs/API.md)
- [架构概览](docs/ARCHITECTURE.md)


---

## 🌐 语言

- [English](README.md)
- [简体中文](README.zh.md)

