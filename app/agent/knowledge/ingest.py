from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import Settings, get_settings


def load_documents(docs_dir: Path | None = None) -> list[Document]:
    """从本地目录加载 .txt / .md 文档。"""
    settings = get_settings()
    root = docs_dir or settings.docs_dir
    root.mkdir(parents=True, exist_ok=True)

    has_files = bool(list(root.rglob("*.md")) or list(root.rglob("*.txt")))
    if not has_files:
        return []

    documents: list[Document] = []
    for pattern in ("**/*.md", "**/*.txt"):
        loader = DirectoryLoader(
            str(root),
            glob=pattern,
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            show_progress=False,
            use_multithreading=True,
        )
        documents.extend(loader.load())
    return documents


def split_documents(
    documents: list[Document],
    settings: Settings | None = None,
) -> list[Document]:
    settings = settings or get_settings()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", "。", "！", "？", "；", " ", ""],
    )
    return splitter.split_documents(documents)
