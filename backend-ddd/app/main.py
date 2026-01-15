# genAI_master_start
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="AI Agent DDD Template", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(chat_router, prefix="/api/v1")
    app.include_router(health_router, prefix="/api/v1")
    return app


app = create_app()
# genAI_master_end
