from langchain.tools import tool

@tool
def test_tool(x: str) -> str:
    return f"Tool is working: {x}"

print(test_tool("Hello"))
