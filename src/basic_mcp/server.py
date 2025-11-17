"""FastMCP server for Azure APIM."""

from fastmcp import FastMCP

# Create the FastMCP instance
mcp = FastMCP("BasicAzureApimMCP")

# Import tools to register them with the MCP instance
# This must be done after creating the mcp instance so the decorators can register
from basic_mcp.tools import sum_tool  # noqa: E402, F401


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
