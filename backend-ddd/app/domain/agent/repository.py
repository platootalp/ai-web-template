# genAI_master_start
from typing import Protocol

from app.domain.agent.entities import AgentMessage


class AgentRepository(Protocol):
    async def save_message(self, message: AgentMessage) -> None: ...
# genAI_master_end
