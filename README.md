# API Generation Agent

[![CI](https://github.com/kogunlowo123/api-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/api-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

API-first development agent that generates RESTful and GraphQL APIs from OpenAPI/GraphQL specifications, including server stubs, client SDKs, validation middleware, rate limiting, and comprehensive API test suites.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_rest_api` | Generate REST API server from OpenAPI specification |
| `generate_graphql_api` | Generate GraphQL API from schema definition |
| `generate_client_sdk` | Generate typed client SDK from API specification |
| `generate_api_tests` | Generate comprehensive API test suite |
| `validate_api_spec` | Validate and lint an API specification |
| `generate_api_gateway_config` | Generate API gateway configuration (Kong, AWS API GW) |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/generate/rest` | Generate REST API from OpenAPI spec |
| `POST` | `/api/v1/generate/graphql` | Generate GraphQL API from schema |
| `POST` | `/api/v1/generate/sdk` | Generate client SDK |
| `POST` | `/api/v1/generate/tests` | Generate API test suite |
| `POST` | `/api/v1/validate` | Validate API specification |

## Features

- Openapi Codegen
- Graphql Codegen
- Sdk Generation
- Validation Middleware
- Rate Limiting
- Api Testing

## Integrations

- Github Connector
- Openapi Parser
- Graphql Parser
- Api Gateway

## Architecture

```
api-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── api_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + OpenAPI Tooling**

---

Built as part of the Enterprise AI Agent Platform.
