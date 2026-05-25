from zai import ZhipuAiClient

from app.config import get_settings

_client: ZhipuAiClient | None = None


def _get_client() -> ZhipuAiClient:
    global _client
    if _client is None:
        settings = get_settings()
        if not settings.zhipu_api_key:
            raise ValueError("请在 .env 中配置 ZHIPU_API_KEY")
        _client = ZhipuAiClient(api_key=settings.zhipu_api_key)
    return _client


def zhipu(question: str) -> str:
    """直接调用智谱大模型（不经过知识库）。"""
    settings = get_settings()
    response = _get_client().chat.completions.create(
        model=settings.zhipu_model,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content
