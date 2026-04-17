import os
import streamlit as st
from src.ingest import ingest_codebase
from src.rag_chain import build_code_explainer_chain, build_rag_chain


st.set_page_config(page_title="AI Codebase Assistant", layout="wide")

st.title("AI Codebase Assistant")
st.subheader("Step 3: RAG over Codebase")

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

mode = st.radio(
    "Choose Mode",
    ["Explain Pasted Code", "Ask Codebase Questions"]
)

if mode == "Explain Pasted Code":
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

else:
    st.write("Ask questions about the indexed codebase.")

    codebase_question = st.text_input(
        "Ask about the codebase",
        value="Where is login logic defined?"
    )

    if st.button("Ask Codebase"):
        try:
            if not os.path.exists("vectorstore/faiss_index"):
                st.warning("Please index the codebase first.")
            else:
                rag_chain = build_rag_chain()
                answer, docs = rag_chain(codebase_question)

                st.success("Answer generated")
                st.write(answer)

                st.subheader("Sources")
                shown = set()
                for doc in docs:
                    source = doc.metadata.get("source", "unknown")
                    if source not in shown:
                        st.write(f"- {source}")
                        shown.add(source)

        except Exception as e:
            st.error(f"Error: {e}")