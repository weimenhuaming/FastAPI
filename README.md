


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
│   └── agent/               # Agent核心包
│       ├── __init__.py
│       ├── rag/             # RAG模块
│       │   ├── __init__.py
│       │   ├── agent.py     # RAG问答逻辑（支持历史）
│       │   ├── llm.py       # LLM封装
│       │   ├── vectorstore.py # 向量库操作
│       │   └── ingest.py    # 文档加载 / chunk / embedding
│       │
│       └── memory/          # 会话 / 多轮上下文管理
│           ├── __init__.py
│           └── session_memory.py
│
└── tests/
    ├── test_chat.py
    ├── test_session.py
    └── test_agent.py
```