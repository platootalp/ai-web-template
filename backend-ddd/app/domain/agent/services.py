# genAI_master_start
from app.domain.agent.entities import AgentMessage
from app.domain.shared.ports import LlmGateway


class AgentService:
    def __init__(self, llm: LlmGateway) -> None:
        self._llm = llm

    async def chat(self, message: AgentMessage) -> str:
        return await self._llm.generate(message.content)
# genAI_master_end
