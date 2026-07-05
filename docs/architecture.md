# API Generation Agent Architecture

API-first development agent that generates RESTful and GraphQL APIs from OpenAPI/GraphQL specifications, including server stubs, client SDKs, validation middleware, rate limiting, and comprehensive API test suites.

## Domain Tools

- **generate_rest_api**: Generate REST API server from OpenAPI specification
- **generate_graphql_api**: Generate GraphQL API from schema definition
- **generate_client_sdk**: Generate typed client SDK from API specification
- **generate_api_tests**: Generate comprehensive API test suite
- **validate_api_spec**: Validate and lint an API specification
- **generate_api_gateway_config**: Generate API gateway configuration (Kong, AWS API GW)