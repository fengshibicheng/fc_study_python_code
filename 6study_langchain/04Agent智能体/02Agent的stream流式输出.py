# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/9
@Auth ： 冯成
@File ： 02Agent的stream流式输出.py
@IDE ： PyCharm
"""
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

@tool(description = "获取股价，传入股票名称，返回字符串信息")
def get_price(name: str) -> str:
    return f"股票{name}的价格是20元"

@tool(description = "获取股票信息，传入股票名称，返回字符串信息")
def get_info(name: str) -> str:
    return f"股票{name}, 是一家A股上市，专注于IT教育"

agent = create_agent(
    model = ChatTongyi(model = "qwen3-max"),
    tools = [get_price, get_info],
    system_prompt = "你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具"
)

for chunk in agent.stream(
    input = {"messages": [{"role": "user", "content": "传智教育的股价是多少，并介绍一下"}]},
    stream_mode = "values"
):
    latest_nessage = chunk['messages'][-1]

    if latest_nessage.content:
        print(type(latest_nessage).__name__, latest_nessage.content)

    try:
        if latest_nessage.tool_calls:
            print(f"工具调用：{ [tc['name'] for tc in latest_nessage.tool_calls] }")
    except AttributeError as e:
        pass
