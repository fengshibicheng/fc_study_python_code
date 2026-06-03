# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 09ChatPromptTemplate的使用.py
@IDE ： PyCharm
"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models import ChatTongyi

# 提示词模版， 列表里面嵌套 元组（）
template = ChatPromptTemplate.from_messages(
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

prompt_text = template.invoke({"history": history_data})
# print(prompt_text.to_string())

# model = Tongyi(model = 'qwen-max')
# res = model.invoke(prompt_text)
# print(res)

model = ChatTongyi(model="qwen3-max")
res = model.invoke(prompt_text)

print(res.content)


