# genAI_master_start
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentMessage:
    role: str
    content: str
# genAI_master_end
