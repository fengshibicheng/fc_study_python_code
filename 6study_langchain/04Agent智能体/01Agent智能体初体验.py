# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/9
@Auth ： fc
@File ： 01Agent智能体初体验.py
@IDE ： PyCharm
"""
"""
    基于外部工具的提供，让大模型拥有了:感知外部世界并影响现实的能力。
    丰富的工具集将极大提升大模型的工作性能和业务范畴。
    工具越多，Agent能覆盖的业务场景就越广(从客服问答到库存管理，再到自动化运营)，性能和实用性自然会大幅提升。
"""
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

@tool(description="查询天气")
def get_weather() -> str:
    return "晴天"

agent = create_agent(
    model = ChatTongyi(model="qwen3-max"),      # 智能体的大脑LLM
    tools = [get_weather],                     # 工具列表
    system_prompt = "你是一个聊天助手，可以回答用户问题。",
)

res = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天深圳的天气如何?"},
        ]
    }
)

# print(res)
for msg in res["messages"]:
    print(f"{type(msg).__name__}:", msg.content)