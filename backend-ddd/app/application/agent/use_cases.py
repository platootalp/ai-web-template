# genAI_master_start
from app.domain.agent.entities import AgentMessage
from app.domain.agent.services import AgentService


class ChatAgentUseCase:
    def __init__(self, agent_service: AgentService) -> None:
        self._agent_service = agent_service

    async def execute(self, message: str) -> str:
        entity = AgentMessage(role="user", content=message)
        return await self._agent_service.chat(entity)
# genAI_master_end
