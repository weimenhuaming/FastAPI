from fastapi import FastAPI
from app.controllers import chat_controller, new_session_controller

app = FastAPI(title="RAG Agent with Knowledge Base")

app.include_router(chat_controller.router)
app.include_router(new_session_controller.router)

@app.get("/health")
def health():
    return {"status": "ok"}