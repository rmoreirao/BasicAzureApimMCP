"""Sum tool for FastMCP server.

This module implements a simple sum tool that adds two numbers together.
"""

from typing import Union

from basic_mcp.server import mcp


def _sum_impl(a: float, b: float) -> float:
    """Implementation of sum logic.

    This function performs addition of two numeric values. It accepts integer or float
    inputs and returns their sum as a float.

    Args:
        a: The first number to add (int or float)
        b: The second number to add (int or float)

    Returns:
        The sum of a and b as a float

    Raises:
        ValueError: If either input is not a numeric type (int or float)

    Examples:
        >>> _sum_impl(2, 3)
        5.0
        >>> _sum_impl(2.5, 3.7)
        6.2
        >>> _sum_impl(-5, 10)
        5.0
        >>> _sum_impl(0, 0)
        0.0
        >>> _sum_impl(1e308, 1e308)  # Very large numbers - may lose precision
        2e+308

    Note:
        - This function uses Python's float type, which has limited precision
          for very large numbers (approximately 15-17 decimal digits).
        - For arbitrary precision arithmetic, consider using Python's decimal module
          (potential future enhancement).
        - Negative numbers and zero are fully supported.
    """
    # Validate that inputs are numeric types
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise ValueError(
            f"First argument 'a' must be a numeric type (int or float), got {type(a).__name__}"
        )
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise ValueError(
            f"Second argument 'b' must be a numeric type (int or float), got {type(b).__name__}"
        )

    # Reject complex numbers explicitly
    if isinstance(a, complex) or isinstance(b, complex):
        raise ValueError("Complex numbers are not supported")

    # Perform the sum - Python will automatically handle int to float conversion
    # Return raw number per requirement (not dict)
    return float(a + b)


@mcp.tool()
def sum(a: float, b: float) -> float:
    """Add two numbers together.

    This tool performs addition of two numeric values. It accepts integer or float
    inputs and returns their sum as a float.

    Args:
        a: The first number to add (int or float)
        b: The second number to add (int or float)

    Returns:
        The sum of a and b as a float

    Raises:
        ValueError: If either input is not a numeric type (int or float)
    """
    return _sum_impl(a, b)
