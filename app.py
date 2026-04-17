import streamlit as st
from src.rag_chain import build_code_explainer_chain


st.set_page_config(page_title="AI Codebase Assistant", layout="wide")

st.title("AI Codebase Assistant")
st.subheader("Step 2: LangChain Code Explanation")

st.write("Paste a code snippet and ask what it does.")

code_input = st.text_area("Paste your code here", height=300)
question = st.text_input("Ask a question about the code", value="Explain this code clearly")

if st.button("Explain Code"):
    if not code_input.strip():
        st.warning("Please paste some code first.")
    else:
        try:
            chain = build_code_explainer_chain()

            response = chain.invoke({
                "question": question,
                "code": code_input
            })

            st.success("Explanation generated")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")