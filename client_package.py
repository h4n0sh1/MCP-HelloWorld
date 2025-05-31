import os
from smolagents import ToolCollection, CodeAgent, InferenceClientModel
from mcp.client.stdio import StdioServerParameters
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')

model = InferenceClientModel(token=token)

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], add_base_tools=True, model=model)
    agent.run("Please find a remedy for hangover.")