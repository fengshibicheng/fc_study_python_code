# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/9
@Auth ： fc
@File ： 03React案例.py
@IDE ： PyCharm
"""
"""
ReAct是一种工作范式，定义了大模型的工作流程。
    思考: 分析需求，考虑下一步
    行动: 工具调用获取信息
    观察: 分析获取的信息
思考->行动->观察->思考...>结束
LangChain的Agent对象，就是按ReAct模式运行。
"""
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langchain.agents import create_agent

@tool(description="获取体重，返回值是整数，单位千克")
def get_weight() -> int:
    return 85

@tool(description="获取身高，返回值是整数，单位厘米")
def get_height() -> int:
    return 188

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    system_prompt="""你是严格遵循ReAct框架的智能体，必须按「思考→行动→观察→再思考」的流程解决问题，
                     且**每轮仅能思考并调用1个工具**，禁止单次调用多个工具。
                     并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我""",
    tools=[get_weight, get_height],
)


for chunk in agent.stream(
    input = {"messages": [{"role": "user", "content": "计算我的BMI"}]},
    stream_mode="values",
):
    latest_message = chunk["messages"][-1]
    if latest_message.content:
        print(latest_message.content.strip())
    try:
        if latest_message.tool_calls:
            print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError:
        pass