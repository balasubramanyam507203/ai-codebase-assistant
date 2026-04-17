from langchain.tools import tool
from src.rag_chain import build_code_explainer_chain, build_rag_chain


@tool
def explain_code_tool(code: str) -> str:
    """
    Use this when the user gives a pasted code snippet and wants an explanation.
    """
    chain = build_code_explainer_chain()
    return chain.invoke({
        "question": "Explain this code clearly",
        "code": code
    })


@tool
def search_codebase_tool(question: str) -> str:
    """
    Use this when the user asks about the indexed codebase, such as where logic is defined,
    how authentication works, or which file contains some feature.
    """
    rag_chain = build_rag_chain()
    answer, docs = rag_chain(question)

    sources = []
    seen = set()
    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        if source not in seen:
            seen.add(source)
            sources.append(source)

    source_text = "\n".join([f"- {s}" for s in sources])

    return f"{answer}\n\nSources:\n{source_text}"


@tool
def find_bug_tool(code: str) -> str:
    """
    Use this when the user wants to find possible bugs, risks, bad practices,
    or suspicious logic in a pasted code snippet.
    """
    chain = build_code_explainer_chain()
    question = """
Find possible bugs, risky logic, bad practices, edge cases, and security issues in this code.
Explain clearly in beginner-friendly language.
"""
    return chain.invoke({
        "question": question,
        "code": code
    })