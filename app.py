import os
import streamlit as st
from src.ingest import ingest_codebase
from src.agent import build_agent


st.set_page_config(page_title="AI Codebase Assistant", layout="wide")

st.title("AI Codebase Assistant")
st.subheader("Step 4: Agent-based Code Assistant")

st.sidebar.header("Codebase Indexing")

default_folder = "data/sample_codebase"
folder_path = st.sidebar.text_input("Codebase folder path", value=default_folder)

if st.sidebar.button("Index Codebase"):
    try:
        result = ingest_codebase(folder_path)
        st.sidebar.success(
            f"Indexed {result['documents_count']} files and {result['chunks_count']} chunks."
        )
    except Exception as e:
        st.sidebar.error(f"Indexing error: {e}")

task_type = st.selectbox(
    "What do you want to do?",
    [
        "Explain pasted code",
        "Ask about indexed codebase",
        "Find bugs in pasted code"
    ]
)

user_input = ""
code_input = ""

if task_type == "Explain pasted code":
    code_input = st.text_area("Paste your code here", height=300)
    user_input = f"Explain this pasted code clearly:\n\n{code_input}"

elif task_type == "Ask about indexed codebase":
    question = st.text_input(
        "Ask a codebase question",
        value="Where is login logic defined?"
    )
    user_input = question

else:
    code_input = st.text_area("Paste code to check for bugs", height=300)
    user_input = f"Find possible bugs, risks, bad practices, edge cases, and security issues in this code:\n\n{code_input}"

if st.button("Run Assistant"):
    try:
        if task_type == "Ask about indexed codebase" and not os.path.exists("vectorstore/faiss_index"):
            st.warning("Please index the codebase first.")

        elif task_type != "Ask about indexed codebase" and not code_input.strip():
            st.warning("Please paste code first.")

        else:
            agent = build_agent()

            response = agent.invoke(
                {
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                }
            )

            st.success("Response generated")

            final_message = response["messages"][-1]
            st.write(final_message.content)

    except Exception as e:
        st.error(f"Error: {e}")