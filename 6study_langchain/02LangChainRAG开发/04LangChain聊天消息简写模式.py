# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： 冯成
@File ： 04LangChain聊天消息简写模式.py
@IDE ： PyCharm
"""
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model = "qwen3-max")

messages = [
    # (角色， 内容)
    ('system', '你是一名诗人'),
    ('human', '请帮我写一首边塞诗'),
    ('ai', '锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦'),
    ('human', '请帮我写一首思乡诗'),
]

res = model.stream(input = messages)

for chunk in res:
    print(chunk.content, end="", flush=True)

