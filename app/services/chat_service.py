# app/services/chat_service.py
from app.agent.llm.zhipu import zhipu
async def chat(user_id: str, question: str):
    res = zhipu(question)
    return res