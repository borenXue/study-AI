
```shell
# 初始化项目
uv init -p cpython-3.13.7
uv venv --python=3.13.7
# source .venv/bin/activate
uv add -r requirements.txt && rm requirements.txt
uv tree -d 2

# 初始化项目 v2
rm -rf .venv
uv sync


# 调试 - 方式1
npx @modelcontextprotocol/inspector --transport stdio python simples/basic_tools.py

# 调试 - 方式2
npx @modelcontextprotocol/inspector --transport stdio uv run simples/basic_tools.py

# 调试 - 方式3
uv run simples/basic_tools.py
npx @modelcontextprotocol/inspector --transport http --server-url http://localhost:8000/mcp 






# 安装依赖
# pip install "mcp[cli]"
```


