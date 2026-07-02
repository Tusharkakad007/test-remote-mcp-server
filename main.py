from fastmcp import FastMCP
import random
import json

# Create FastMCP server
mcp = FastMCP("Sample Calculator Server")


@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers.
    """
    return a + b


@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random number.

    Args:
        min_val: Minimum value.
        max_val: Maximum value.

    Returns:
        Random integer between min_val and max_val.
    """

    if min_val > max_val:
        raise ValueError("min_val must be less than or equal to max_val")

    return random.randint(min_val, max_val)


@mcp.resource("info://server")
def server_info() -> str:
    """Return server information."""

    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Tushar Kakad"
    }

    return json.dumps(info, indent=4)


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )