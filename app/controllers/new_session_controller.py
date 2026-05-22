# app/controllers/session_controller.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.new_session_service import reset_session

router = APIRouter()

class NewSessionRequest(BaseModel):
    user_id: str

class NewSessionResponse(BaseModel):
    message: str

@router.post("/new_chat", response_model=NewSessionResponse)
def new_chat_endpoint(req: NewSessionRequest):
    reset_session(req.user_id)
    return NewSessionResponse(message="新对话已创建")