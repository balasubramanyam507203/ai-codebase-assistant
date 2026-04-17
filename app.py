import streamlit as st
from src.llm import get_llm


st.set_page_config(page_title="AI Codebase Assistant", layout="wide")

st.title("AI Codebase Assistant")
st.subheader("Step 1: Basic Code Explanation")

st.write("Paste a code snippet and ask what it does.")

code_input = st.text_area("Paste your code here", height=300)
question = st.text_input("Ask a question about the code", value="Explain this code clearly")

if st.button("Explain Code"):
    if not code_input.strip():
        st.warning("Please paste some code first.")
    else:
        try:
            llm = get_llm()

            prompt = f"""
You are a helpful coding assistant.

Explain the following code in a beginner-friendly way.

User question:
{question}

Code:
{code_input}
"""

            response = llm.invoke(prompt)

            st.success("Explanation generated")
            st.write(response.content)

        except Exception as e:
            st.error(f"Error: {e}")