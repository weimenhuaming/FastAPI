import asyncio
from functools import partial

from app.agent.knowledge.builder import rebuild_knowledge_base


async def rebuild() -> dict:
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, rebuild_knowledge_base)
    return result
