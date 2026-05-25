from typing import Any

from langchain_core.language_models.llms import LLM
from langchain_core.callbacks import CallbackManagerForLLMRun

from app.agent.llm.zhipu import zhipu


class ZhipuLangChainLLM(LLM):
    """将智谱 SDK 封装为 LangChain LLM，供 RetrievalQA 使用。"""

    @property
    def _llm_type(self) -> str:
        return "zhipu"

    def _call(
        self,
        prompt: str,
        stop: list[str] | None = None,
        run_manager: CallbackManagerForLLMRun | None = None,
        **kwargs: Any,
    ) -> str:
        return zhipu(prompt)
