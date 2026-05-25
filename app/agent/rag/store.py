from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStore

from app.agent.knowledge.embeddings import get_embeddings
from app.config import Settings, get_settings


def get_chroma_store(
    persist_dir: Path | None = None,
    settings: Settings | None = None,
) -> Chroma | None:
    """读取已构建的 Chroma 向量库（只读）。"""
    settings = settings or get_settings()
    path = persist_dir or settings.chroma_persist_dir
    if not path.exists():
        return None
    store = Chroma(
        persist_directory=str(path),
        embedding_function=get_embeddings(settings),
        collection_name="knowledge_base",
    )
    if store._collection.count() == 0:
        return None
    return store


def get_vector_store() -> VectorStore | None:
    return get_chroma_store()
