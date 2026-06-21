# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/9
@Auth ： fc
@File ： 04middleware中间件使用.py
@IDE ： PyCharm
"""
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool
from langchain.agents import create_agent, AgentState
from langgraph.runtime import Runtime
"""
1、agent执行前
2、agent执行后
3、model执行前
4、model执行后
5、工具执行中
6、模型执行中
"""

#  定义天气查询工具
@tool(description="查询天气，传入城市名称字符串，返回字符串天气信息")
def get_weather(city) -> str:
    return f"{city},晴天"


# 1. 【agent执行前】智能体执行前的钩子（Agent 启动时触发）
@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_agent]agent启动，并附带 {len(state['messages'])} 消息")


# 2. 【agent执行后】智能体执行完成后的钩子（Agent 结束时触发）
@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_agent]agent结束，并附带 {len(state['messages'])} 消息")


# 3. 【model执行前】调用大模型前的钩子（每次调用 LLM 前触发）
@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_model]模型即将调用，并附带 {len(state['messages'])} 消息")


# 4. 【model执行后】调用大模型后的钩子（每次调用 LLM 后触发）
@after_model
# def log_latest_message(state: AgentState, runtime: Runtime) -> None:
#     print("after_model", state["messages"][-1].content)
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_model]模型调用结束，并附带 {len(state['messages'])} 消息")

# 5. 【工具执行中】
@wrap_tool_call
def monitor_tool(request, handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入参数：{request.tool_call['args']}")

    return handler(request)

# 6. 【模型执行中】
@wrap_model_call
def mode_call_hook(request, handler):
    print("模型调用啦")
    return handler(request)

# 创建智能体
agent = create_agent(
    model = ChatTongyi(model = "qwen3-max"),
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, log_before_model, log_after_model, monitor_tool,  mode_call_hook],
)

res = agent.invoke({"messages": [{"role": "user", "content": "深圳今天天气如何呀，如何穿衣"}]})
print("*********\n", res)