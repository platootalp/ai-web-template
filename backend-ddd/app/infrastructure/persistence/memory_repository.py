# genAI_master_start
from app.domain.agent.entities import AgentMessage
from app.domain.agent.repository import AgentRepository


class InMemoryAgentRepository(AgentRepository):
    def __init__(self) -> None:
        self._messages: list[AgentMessage] = []

    async def save_message(self, message: AgentMessage) -> None:
        self._messages.append(message)
# genAI_master_end
