from app.agent.knowledge.chroma import build_chroma_index
from app.agent.knowledge.ingest import load_documents, split_documents
from app.config import get_settings


def rebuild_knowledge_base() -> dict:
    """加载文档 → 切分 → 写入 Chroma 向量库。"""
    settings = get_settings()
    docs = load_documents()
    if not docs:
        return {
            "ok": False,
            "message": f"未在 {settings.docs_dir} 找到 .txt/.md 文档，请先放入知识库文件",
            "chunks": 0,
        }

    chunks = split_documents(docs, settings)
    build_chroma_index(chunks, settings)

    return {
        "ok": True,
        "message": "知识库构建完成",
        "source_files": len(docs),
        "chunks": len(chunks),
        "vector_store": "chroma",
    }
