from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import get_llm


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

    chain = prompt | llm | parser
    return chain