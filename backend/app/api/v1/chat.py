# genAI_master_start
from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import run_agent

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    result = await run_agent(request.message)
    return ChatResponse(reply=result)
# genAI_master_end
