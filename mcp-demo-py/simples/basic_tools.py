from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="XbrDemo")

@mcp.tool(name="加法计算")
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 1

@mcp.tool()
def get_weather(city: str, unit: str = "celsius") -> str:
    """Get weather for a city."""
    return f"{city}今天的天气: 你猜~_~"

if __name__ == "__main__":
    # mcp.run(transport='stdio')
    mcp.run(transport='sse')
