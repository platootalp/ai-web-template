# AI Agent 前后端分离模板（Python + TypeScript）

面向大模型 Agent 应用的现代全栈模板，包含 FastAPI + LangChain 后端与 React + Vite + Tailwind + TanStack Query
前端示例，仅提供结构与样例代码，适合二次扩展。

## 技术栈

- 后端：FastAPI + LangChain + Pydantic + Uvicorn + uv
- 前端：React + TypeScript + Vite + Tailwind CSS + TanStack Query

## 目录结构

```
web-application-template
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── v1
│   │   │   │   ├── __init__.py
│   │   │   │   └── chat.py
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── chat.py
│   │   │   └── common.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   └── agent_service.py
│   │   ├── utils
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_health.py
│   ├── env.example
│   ├── pyproject.toml
│   └── requirements.txt
├── backend-ddd
│   ├── app
│   │   ├── api
│   │   │   └── v1
│   │   │       ├── __init__.py
│   │   │       ├── chat.py
│   │   │       └── health.py
│   │   ├── application
│   │   │   └── agent
│   │   │       ├── __init__.py
│   │   │       └── use_cases.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── domain
│   │   │   ├── agent
│   │   │   │   ├── __init__.py
│   │   │   │   ├── entities.py
│   │   │   │   ├── repository.py
│   │   │   │   └── services.py
│   │   │   └── shared
│   │   │       ├── __init__.py
│   │   │       └── ports.py
│   │   ├── infrastructure
│   │   │   ├── llm
│   │   │   │   ├── __init__.py
│   │   │   │   └── langchain_gateway.py
│   │   │   └── persistence
│   │   │       ├── __init__.py
│   │   │       └── memory_repository.py
│   │   ├── interfaces
│   │   │   └── http
│   │   │       ├── __init__.py
│   │   │       ├── controllers.py
│   │   │       └── schemas.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_health.py
│   ├── env.example
│   ├── pyproject.toml
│   └── requirements.txt
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   │   └── ChatCard.tsx
│   │   ├── hooks
│   │   │   └── useAgentChat.ts
│   │   ├── pages
│   │   │   └── ChatPage.tsx
│   │   ├── services
│   │   │   └── api.ts
│   │   ├── types
│   │   │   └── index.ts
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── index.html
│   ├── postcss.config.cjs
│   ├── tailwind.config.ts
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── package.json
├── frontend-vue
│   ├── public
│   ├── src
│   │   ├── components
│   │   │   └── ChatCard.vue
│   │   ├── composables
│   │   │   └── useAgentChat.ts
│   │   ├── pages
│   │   │   └── ChatPage.vue
│   │   ├── services
│   │   │   └── api.ts
│   │   ├── types
│   │   │   └── index.ts
│   │   ├── App.vue
│   │   ├── index.css
│   │   └── main.ts
│   ├── index.html
│   ├── postcss.config.cjs
│   ├── tailwind.config.ts
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── package.json
└── README.md
```

## 快速开始

### 后端（uv）

```
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

### 后端（DDD 模板）

```
cd backend-ddd
uv sync
uv run uvicorn app.main:app --reload
```

### 前端

```
cd frontend
npm install
npm run dev
```

### 前端（Vue 模板）

```
cd frontend-vue
npm install
npm run dev
```

> 默认前端请求 `http://localhost:8000/api/v1`，可通过 `VITE_API_BASE` 覆盖。

## API 示例

- `GET /api/health`：健康检查
- `POST /api/v1/chat`：Agent 聊天接口

请求体：

```
{
  "message": "请介绍项目定位"
}
```

响应体：

```
{
  "reply": "..."
}
```

## 环境变量

后端示例文件 `backend/env.example`：

```
OPENAI_API_KEY=sk-please_replace
MODEL_NAME=gpt-4o
```

## 说明

- `agent_service.py` 使用 LangChain 的工具调用 Agent 作为示例，可替换为你的 Prompt/Tool/Graph 方案。
- 若需容器化或多环境部署，可增加 `docker-compose.yml` 与 Nginx 配置。
