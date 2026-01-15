# genAI_master_start
from app.application.agent.use_cases import ChatAgentUseCase
from app.domain.agent.entities import AgentMessage
from app.domain.agent.services import AgentService
from app.infrastructure.llm.langchain_gateway import LangChainGateway
from app.infrastructure.persistence.memory_repository import InMemoryAgentRepository


class AgentController:
    def __init__(self) -> None:
        repository = InMemoryAgentRepository()
        llm_gateway = LangChainGateway()
        service = AgentService(llm_gateway)
        self._use_case = ChatAgentUseCase(service)
        self._repository = repository

    async def chat(self, message: str) -> str:
        reply = await self._use_case.execute(message)
        await self._repository.save_message(AgentMessage(role="user", content=message))
        await self._repository.save_message(
            AgentMessage(role="assistant", content=reply)
        )
        return reply
# genAI_master_end
