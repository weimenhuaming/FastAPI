import asyncio
from functools import partial

from app.agent.llm.zhipu import zhipu
from app.agent.rag.qa_chain import rag_answer


async def chat_with_rag(question: str) -> dict:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, partial(rag_answer, question))


async def chat(user_id: str, question: str, use_rag: bool = True) -> dict:
    if use_rag:
        return await chat_with_rag(question)
    loop = asyncio.get_event_loop()
    answer = await loop.run_in_executor(None, partial(zhipu, question))
    return {"answer": answer, "mode": "direct"}
