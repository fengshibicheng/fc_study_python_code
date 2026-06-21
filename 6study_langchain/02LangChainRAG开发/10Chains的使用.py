# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： fc
@File ： 10Chains的使用.py
@IDE ： PyCharm
"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models import ChatTongyi

# 提示词模版， 列表里面嵌套 元组（）
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', "你是一个边塞诗人，可以作诗"),
        MessagesPlaceholder("history"),
        ('human', "请再来一首唐诗")
    ]
)

history_data = [
    ('human', "你来做一首唐诗"),
    ('ai', "窗前明月光，疑是地上霜"),
    ('human', "很好，很好，再来一首"),
    ('ai', "举头望明月，低头思故乡"),
]

model = ChatTongyi(model = 'qwen3-max')

# 组成一个链 , 要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | model

# 1、通过链去调用 invoke或者stream    原始输入字典
# res = chain.invoke({"history": history_data})
# print(res.content)

# 2、通过流式输出进行调用stream，一个字一个字蹦出来，能够表明模型一步一步思考的过程
# res = chain.stream({"history": history_data})
# for chunk in res:

for chunk in chain.stream(input = {"history": history_data}):
    print(chunk.content, end="", flush=True)