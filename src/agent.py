from langchain.agents import create_agent
from src.tools import explain_code_tool, search_codebase_tool, find_bug_tool


def build_agent():
    tools = [
        explain_code_tool,
        search_codebase_tool,
        find_bug_tool,
    ]

    agent = create_agent(
        model="openai:gpt-4o-mini",
        tools=tools,
        system_prompt=(
            "You are an AI code assistant. "
            "Choose the best available tool for the user's request. "
            "Use explain_code_tool for pasted code explanations, "
            "search_codebase_tool for questions about the indexed codebase, "
            "and find_bug_tool for bug/risk analysis."
        ),
    )

    return agent