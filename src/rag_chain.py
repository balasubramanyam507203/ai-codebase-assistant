from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import get_llm
from src.retriever import load_retriever


def build_code_explainer_chain():
    prompt = PromptTemplate(
        input_variables=["question", "code"],
        template="""
You are a helpful coding assistant.

Explain the following code in a beginner-friendly and clear way.

User question:
{question}

Code:
{code}

Give:
1. What the code does
2. Line-by-line explanation
3. Any important logic used
4. Possible improvements if needed
"""
    )

    llm = get_llm()
    parser = StrOutputParser()
    return prompt | llm | parser


def build_rag_chain():
    retriever = load_retriever()
    llm = get_llm()
    parser = StrOutputParser()

    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="""
You are an AI codebase assistant.

Answer the user's question only using the retrieved code context below.

If the answer is not in the context, say:
"I could not find that in the indexed codebase."

Question:
{question}

Retrieved context:
{context}

Give a clear and beginner-friendly answer.
"""
    )

    def format_docs(docs):
        return "\n\n".join(
            [f"Source: {doc.metadata.get('source', 'unknown')}\n{doc.page_content}" for doc in docs]
        )

    def rag_invoke(question: str):
        docs = retriever.invoke(question)
        context = format_docs(docs)
        answer = (prompt | llm | parser).invoke({
            "question": question,
            "context": context
        })
        return answer, docs

    return rag_invoke