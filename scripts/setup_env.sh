#!/usr/bin/env bash
# 必须先激活你自己的 conda/venv，再执行本脚本
# 示例：conda activate agent && bash scripts/setup_env.sh
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -z "${CONDA_DEFAULT_ENV:-}" && -z "${VIRTUAL_ENV:-}" ]]; then
  echo "请先激活虚拟环境，例如: conda activate agent"
  exit 1
fi

PYTHON="$(which python)"
echo "当前 Python: $PYTHON"

if ! python -c "import poetry" 2>/dev/null; then
  echo "正在向当前环境安装 poetry..."
  pip install poetry
fi

python -m poetry env use "$PYTHON"
python -m poetry install

echo "完成。可直接运行: uvicorn app.main:app --reload"
