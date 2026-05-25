
# RAG Agent（FastAPI + LangChain + Chroma）

基于知识库的问答服务：文档切分 → 向量检索 → 智谱大模型生成。

## 环境准备（Poetry 管理依赖，装进你自己的 Python 环境）

本项目 **不** 使用项目内 `.venv`。`poetry install` 会把包装进你通过 `poetry env use` 绑定的解释器里（例如 conda 的 `agent`）。

### 本机（conda 环境名 `agent`）

```bash
conda activate agent
cd /Users/edy/GolandProjects/Agent

pip install poetry                      # 把 poetry 装进 agent（首次）
python -m poetry env use "$(which python)"
python -m poetry install                # 依赖装进 agent

cp .env.example .env                    # 填写 ZHIPU_API_KEY
```

之后 **在 agent 里直接启动**（无需 `poetry run`）：

```bash
conda activate agent
uvicorn app.main:app --reload
```

一键安装：`conda activate agent && bash scripts/setup_env.sh`

> **重要**：请用 `python -m poetry install`，不要用全局 `~/.local/bin/poetry`，否则可能装到 conda 根环境而不是 `agent`。

### 其他人克隆项目后

各自创建并激活 **自己的** conda/venv，再执行同样步骤：

```bash
conda create -n myenv python=3.12 -y   # 环境名随意
conda activate myenv
cd Agent
pip install poetry
python -m poetry env use "$(which python)"
python -m poetry install
```

> 不创建项目 `.venv`；`poetry install` 装进 **当前已激活环境** 的 `site-packages`。

在 `.env` 中配置：

- `ZHIPU_API_KEY`：智谱 API Key（必填）
- 其余项有默认值，可按需调整

```
ZHIPU_API_KEY=你的智谱Key
ZHIPU_MODEL=glm-4-plus
DOCS_DIR=data/docs
CHROMA_PERSIST_DIR=data/chroma_db
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
CHUNK_SIZE=500
CHUNK_OVERLAP=50
RETRIEVAL_K=4
```

## 快速开始

```bash
# 1. 将 .md / .txt 放入 data/docs（已附带示例 project_intro.md）

# 2. 构建向量库（先 conda activate agent）
python scripts/build_knowledge.py
# 或启动服务后: curl -X POST http://127.0.0.1:8000/knowledge/rebuild

# 3. 启动 API
uvicorn app.main:app --reload

# 4. 知识库问答
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":"u1","question":"本项目用的向量库是什么？","use_rag":true}'
```

## 目录结构

```text
rag-agent/
├── pyproject.toml
├── README.md
├── .env
├── data/docs/               # Markdown / 文本资料
│
├── app/
│   ├── __init__.py
│   ├── config.py            # 配置管理（读取.env）
│   ├── main.py              # FastAPI入口，注册路由
│
│   ├── controllers/         # 控制层
│   │   ├── __init__.py
│   │   ├── chat_controller.py
│   │   └── session_controller.py
│
│   ├── services/            # 业务逻辑层
│   │   ├── __init__.py
│   │   ├── chat_service.py
│   │   └── session_service.py
│
│   ├── models/              # 数据模型（可选持久化）
│   │   ├── __init__.py
│   │   └── session.py
│
│   └── agent/
│       ├── knowledge/           # 向量库构建（文档加载、切分、写入 Chroma）
│       │   ├── ingest.py
│       │   ├── chroma.py
│       │   └── builder.py
│       ├── llm/                 # 大模型调用
│       │   ├── zhipu.py
│       │   └── prompt.py
│       └── rag/                 # 检索与问答编排
│           ├── store.py         # 读取 Chroma
│           ├── retriever.py     # 相似度检索
│           └── qa_chain.py      # 检索 + LLM 生成
│
└── tests/
    ├── test_chat.py
    ├── test_session.py
    └── test_agent.py
```