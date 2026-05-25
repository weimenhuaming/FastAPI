#!/usr/bin/env python3
"""命令行构建知识库：poetry run python scripts/build_knowledge.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.agent.knowledge.builder import rebuild_knowledge_base


def main() -> None:
    result = rebuild_knowledge_base()
    print(result)
    if result.get("ok"):
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
