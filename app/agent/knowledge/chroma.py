import shutil

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore

from app.agent.knowledge.embeddings import get_embeddings
from app.config import Settings, get_settings


def build_chroma_index(
    chunks: list[Document],
    settings: Settings | None = None,
) -> VectorStore:
    """将文本片段写入 Chroma 向量库。"""
    settings = settings or get_settings()
    persist_dir = settings.chroma_persist_dir
    if persist_dir.exists():
        for child in persist_dir.iterdir():
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                shutil.rmtree(child)

    return Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(settings),
        persist_directory=str(persist_dir),
        collection_name="knowledge_base",
    )
