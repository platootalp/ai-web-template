# genAI_master_start
from typing import Protocol


class LlmGateway(Protocol):
    async def generate(self, prompt: str) -> str: ...
# genAI_master_end
