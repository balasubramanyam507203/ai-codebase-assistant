from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def load_code_documents(folder_path: str):
    documents = []
    allowed_extensions = {".py", ".js", ".ts", ".java", ".cpp", ".c", ".md"}

    folder = Path(folder_path)

    for file_path in folder.rglob("*"):
        if file_path.is_file() and file_path.suffix in allowed_extensions:
            try:
                content = file_path.read_text(encoding="utf-8")
                documents.append(
                    Document(
                        page_content=content,
                        metadata={"source": str(file_path)}
                    )
                )
            except Exception as e:
                print(f"Could not read {file_path}: {e}")

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    return splitter.split_documents(documents)


def create_vectorstore(chunks, save_path="vectorstore/faiss_index"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(save_path)
    return vectorstore


def ingest_codebase(folder_path: str, save_path="vectorstore/faiss_index"):
    documents = load_code_documents(folder_path)
    chunks = split_documents(documents)
    vectorstore = create_vectorstore(chunks, save_path)

    return {
        "documents_count": len(documents),
        "chunks_count": len(chunks),
        "vectorstore": vectorstore
    }