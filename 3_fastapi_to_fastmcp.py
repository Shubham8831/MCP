# we can easily convert fast api to a fast mcp
from fastmcp import FastMCP
from main import app # this is the fastapi app

#convert FastAPI to FastMCP
mcp = FastMCP.from_fastapi(
    app=app,
    name="expense tracker server"
)

if __name__=="__main__":
    mcp.run()

# now it will run like normal mcp server run inspector, run server, connect server