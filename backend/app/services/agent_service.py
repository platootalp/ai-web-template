# genAI_master_start
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.core.config import settings


def get_agent_executor() -> AgentExecutor:
    llm = ChatOpenAI(model=settings.model_name, temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个高效的AI助手，回答简洁清晰。"),
            ("user", "{input}"),
        ]
    )
    agent = create_tool_calling_agent(llm, tools=[], prompt=prompt)
    return AgentExecutor(agent=agent, tools=[], verbose=True)


async def run_agent(message: str) -> str:
    executor = get_agent_executor()
    result = await executor.ainvoke({"input": message})
    return str(result.get("output", ""))
# genAI_master_end
