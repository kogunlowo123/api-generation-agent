"""API Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_rest_api():
    """Test Generate REST API server from OpenAPI specification."""
    tools = AgentTools()
    result = await tools.generate_rest_api(openapi_spec="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_graphql_api():
    """Test Generate GraphQL API from schema definition."""
    tools = AgentTools()
    result = await tools.generate_graphql_api(schema="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_client_sdk():
    """Test Generate typed client SDK from API specification."""
    tools = AgentTools()
    result = await tools.generate_client_sdk(spec="test", target_language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_api_tests():
    """Test Generate comprehensive API test suite."""
    tools = AgentTools()
    result = await tools.generate_api_tests(spec="test", test_framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.api_generation_agent_agent import ApiGenerationAgentAgent
    agent = ApiGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
