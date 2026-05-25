from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.chat_service import chat

router = APIRouter()


class ChatRequest(BaseModel):
    user_id: str
    question: str
    use_rag: bool = Field(default=True, description="True=知识库问答，False=直接调用大模型")


class ChatResponse(BaseModel):
    code: int
    message: str | dict


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    res = await chat(req.user_id, req.question, use_rag=req.use_rag)
    return ChatResponse(code=200, message=res)

