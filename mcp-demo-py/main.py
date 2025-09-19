from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="XbrDemo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 1

@mcp.tool()
def get_weather(city: str, unit: str = "celsius") -> str:
    """Get weather for a city."""
    return f"Weather in {city}: 22degrees{unit[0].upper()}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
