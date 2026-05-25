# RAG Agent 项目说明

本项目是一个基于 FastAPI 的 RAG（检索增强生成）问答服务。

## 技术栈

- **Web 框架**：FastAPI + Uvicorn
- **大模型**：智谱 GLM（zai-sdk）
- **RAG 框架**：LangChain
- **向量库**：Chroma
- **文本切分**：RecursiveCharacterTextSplitter
- **嵌入模型**：sentence-transformers 多语言 MiniLM

## 主要 API

| 接口 | 说明 |
|------|------|
| POST /knowledge/rebuild | 从 data/docs 加载文档并构建向量库 |
| POST /chat | 问答（use_rag=true 走知识库，false 直连大模型） |
| POST /new_chat | 新建会话（预留） |

## 使用步骤

1. 在 `.env` 配置 `ZHIPU_API_KEY`
2. 将 `.txt` / `.md` 文档放入 `data/docs`
3. 调用 `POST /knowledge/rebuild` 构建知识库
4. 调用 `POST /chat` 提问

## 向量库配置

使用 Chroma，数据持久化在 `data/chroma_db`（可通过 `CHROMA_PERSIST_DIR` 配置）。
