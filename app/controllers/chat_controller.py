# app/controllers/chat_controller.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import chat

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    question: str

class ChatResponse(BaseModel):
    code: int
    message: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    res = chat(req.user_id, req.question)
    return ChatResponse(code=200,message=res)