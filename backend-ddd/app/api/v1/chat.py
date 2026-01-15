# genAI_master_start
from fastapi import APIRouter

from app.interfaces.http.schemas import ChatRequest, ChatResponse
from app.interfaces.http.controllers import AgentController

router = APIRouter()
controller = AgentController()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    reply = await controller.chat(request.message)
    return ChatResponse(reply=reply)
# genAI_master_end
