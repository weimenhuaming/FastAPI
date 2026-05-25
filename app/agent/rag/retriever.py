from langchain_core.documents import Document

from app.agent.rag.store import get_vector_store
from app.config import get_settings


def retrieve_documents(question: str) -> list[Document]:
    """从向量库检索与问题相关的文档片段；无库时返回空列表。"""
    store = get_vector_store()
    if store is None:
        return []

    settings = get_settings()
    return store.similarity_search(question, k=settings.retrieval_k)
