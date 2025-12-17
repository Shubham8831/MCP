#demo REMOTE MCP SERVER

from fastmcp import FastMCP
import random
import json

#create a mcp instance

mcp = FastMCP("simple calculator")

# add 2 number
@mcp.tool
def add(a:int, b:int) ->int:
    "add two numnber together"
    return a+b

# generate random number
@mcp.tool
def generate_random_number(min: int = 1, max: int = 100) -> int:
    "generate a random number within that range"
    return random.randint(min, max)

#resource - server info
@mcp.resource("info://server")
def server_information()-> str:
    "get information about the server"
    info = {
        "name" : "demo calculator server",
        "version": "1.0.0",
        "description": "basic mcp server with math tool",
        "tools": ["add", "random_number"],
        "author":"shu"
    }
    return json.dumps(info, indent=2)



if __name__=="__main__":
    mcp.run(transport="http", host = "0.0.0.0", port=8000)
    # mcp.run() is for transport stdio and now we set it as http for remote mcp server


    # Deploy on FastMCP cloud and open add add custom connectors in claude desktop (no in free plan) :/