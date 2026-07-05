"""Test configuration for API Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "api-generation-agent", "category": "Software Engineering"}
