# genAI_master_start
from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.domain.shared.ports import LlmGateway


class LangChainGateway(LlmGateway):
    def __init__(self) -> None:
        self._client = ChatOpenAI(model=settings.model_name, temperature=0)

    async def generate(self, prompt: str) -> str:
        response = await self._client.ainvoke(prompt)
        return response.content
# genAI_master_end
