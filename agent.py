from google.adk.agents.llm_agent import Agent

from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from mcp import StdioServerParameters


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions related to K-Beauty .',
    instruction='Answer user questions to the best of your knowledge',
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command="python3",
                    args=["/home/madhu_712/k-beauty-mcp/kbeautymcpserver.py"],
                    cwd= "/home/madhu_712/k-beauty-mcp/"
                )
            )
        )
    ]
                    
)
