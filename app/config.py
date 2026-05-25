from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    zhipu_api_key: str = ""
    zhipu_model: str = "glm-4-plus"

    docs_dir: Path = PROJECT_ROOT / "data" / "docs"
    chroma_persist_dir: Path = PROJECT_ROOT / "data" / "chroma_db"
    embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    chunk_size: int = 500
    chunk_overlap: int = 50
    retrieval_k: int = 4


@lru_cache
def get_settings() -> Settings:
    return Settings()
