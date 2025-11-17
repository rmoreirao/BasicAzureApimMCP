# BasicAzureApimMCP

A FastMCP server implementation with basic tools for Azure APIM integration.

## Features

- **Sum Tool**: A simple MCP tool that adds two numbers together
  - Supports integers and floats
  - Input validation with clear error messages
  - Type hints compatible with mypy strict mode

## Installation

```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Usage

### Running the Server

```python
from basic_mcp.server import mcp

# Run the MCP server
mcp.run()
```

Or from command line:
```bash
python -m basic_mcp.server
```

### Using the Sum Tool

The sum tool is available through the FastMCP interface:

```python
import asyncio
from basic_mcp.server import mcp

async def example():
    # Get the tool
    tool = await mcp.get_tool("sum")
    
    # Call the tool function directly
    result = tool.fn(2.0, 3.0)
    print(f"2 + 3 = {result}")  # Output: 2 + 3 = 5.0

asyncio.run(example())
```

### Examples

```python
# Basic addition
sum(2, 3)  # Returns 5.0

# Float addition
sum(2.5, 3.7)  # Returns 6.2

# Negative numbers
sum(-5, 10)  # Returns 5.0

# Zero values
sum(0, 0)  # Returns 0.0

# Very large numbers (note: limited precision)
sum(1e308, 1e308)  # Returns 2e+308
```

### Input Validation

The sum tool validates inputs and raises `ValueError` for invalid types:

```python
sum("2", 3)  # Raises ValueError: must be a numeric type
sum(None, 3)  # Raises ValueError: must be a numeric type
sum(True, 3)  # Raises ValueError: must be a numeric type
```

## Development

### Running Tests

```bash
# Set PYTHONPATH and run all tests
export PYTHONPATH=src:$PYTHONPATH
pytest tests/ -v
```

### Project Structure

```
BasicAzureApimMCP/
├── src/
│   └── basic_mcp/
│       ├── __init__.py
│       ├── server.py          # FastMCP server instance
│       └── tools/
│           ├── __init__.py
│           └── sum_tool.py    # Sum tool implementation
├── tests/
│   ├── test_sum_tool.py       # Unit tests
│   └── test_sum_integration.py # Integration tests
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Requirements

- Python >= 3.10
- fastmcp >= 0.1.0

## License

See LICENSE file for details.
