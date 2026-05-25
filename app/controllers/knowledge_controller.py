from fastapi import APIRouter
from pydantic import BaseModel

from app.services.knowledge_service import rebuild

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


class RebuildResponse(BaseModel):
    code: int
    data: dict


@router.post("/rebuild", response_model=RebuildResponse)
async def rebuild_knowledge():
    """加载 data/docs 文档并重建向量库。"""
    data = await rebuild()
    return RebuildResponse(code=200, data=data)
