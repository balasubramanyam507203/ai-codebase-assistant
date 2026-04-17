from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def load_retriever(save_path="vectorstore/faiss_index"):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    return retriever