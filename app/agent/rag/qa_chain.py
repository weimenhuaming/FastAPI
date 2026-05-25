from langchain_core.documents import Document

from app.agent.llm.prompt import RAG_QA_TEMPLATE
from app.agent.llm.zhipu import zhipu
from app.agent.rag.retriever import retrieve_documents

# 格式化文档内容，方便投喂
def _format_context(docs: list[Document]) -> str:
    if not docs:
        return "（暂无相关资料）"
    parts = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "未知来源")
        parts.append(f"[{i}] 来源: {source}\n{doc.page_content}")
    return "\n\n".join(parts)



def rag_answer(question: str) -> dict:
    """
    优先检索知识库作为参考；无检索结果时直接由大模型回答。
    """

    # 从知识库中获取知识
    docs = retrieve_documents(question)
    if not docs:
        return {
            "answer": zhipu(question),
            "mode": "llm_only",
        }

    context = _format_context(docs)

    # 将检索到的知识与问题一起构造成提示词，供大模型生成答案
    prompt = RAG_QA_TEMPLATE.format(context=context, question=question)

    return {
        "answer": zhipu(prompt),
        "mode": "rag_reference",
    }
