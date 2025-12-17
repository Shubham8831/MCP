# to add remote mcp server with claude in free plan 

from fastmcp import FastMCP

# Create a proxy to your remote FastMCP Cloud server
# FastMCP Cloud uses Streamable HTTP (default), so just use the /mcp URL
mcp = FastMCP.as_proxy(
    "https://formal-maroon-cattle.fastmcp.app/mcp",  # Standard FastMCP Cloud URL
    name="Nitish Server Proxy"
)

if __name__ == "__main__":
    # This runs via STDIO, which Claude Desktop can connect to
    mcp.run()