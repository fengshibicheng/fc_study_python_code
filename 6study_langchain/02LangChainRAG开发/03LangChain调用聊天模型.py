# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： fc
@File ： 03LangChain调用聊天模型.py
@IDE ： PyCharm
"""
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# qwen3-max是聊天模型，qwen-max是大语言模型
model = ChatTongyi(model = "qwen3-max")

messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content= "写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="请你按照上一个回复的格式，在写一首唐诗。")
]

res = model.stream(messages)

for chunk in res:
    print(chunk.content, end="", flush=True)