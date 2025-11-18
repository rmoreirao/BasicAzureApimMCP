"""Integration test for sum tool via MCP client interface."""

import asyncio
import pytest

from basic_mcp.server import mcp


class TestSumToolIntegration:
    """Integration tests for sum tool through MCP interface."""

    @pytest.mark.asyncio
    async def test_sum_tool_via_mcp_get_tool(self):
        """Test that sum tool can be retrieved via MCP."""
        tool = await mcp.get_tool("sum")
        assert tool is not None
        assert tool.name == "sum"

    @pytest.mark.asyncio
    async def test_sum_tool_parameters(self):
        """Test that sum tool has correct parameters."""
        tool = await mcp.get_tool("sum")
        assert "a" in tool.parameters["properties"]
        assert "b" in tool.parameters["properties"]
        assert tool.parameters["properties"]["a"]["type"] == "number"
        assert tool.parameters["properties"]["b"]["type"] == "number"

    @pytest.mark.asyncio
    async def test_sum_tool_callable(self):
        """Test that sum tool function can be called."""
        tool = await mcp.get_tool("sum")
        # The tool.fn is the wrapped function
        result = tool.fn(2.0, 3.0)
        assert result == 5.0

    @pytest.mark.asyncio
    async def test_sum_tool_with_negative_numbers(self):
        """Test sum tool with negative numbers."""
        tool = await mcp.get_tool("sum")
        result = tool.fn(-5.0, 10.0)
        assert result == 5.0

    @pytest.mark.asyncio
    async def test_sum_tool_with_floats(self):
        """Test sum tool with float numbers."""
        tool = await mcp.get_tool("sum")
        result = tool.fn(2.5, 3.7)
        assert result == 6.2

    @pytest.mark.asyncio
    async def test_sum_tool_validation_error(self):
        """Test that sum tool raises ValueError for invalid inputs."""
        tool = await mcp.get_tool("sum")
        with pytest.raises(ValueError, match="must be a numeric type"):
            tool.fn("2", 3.0)
