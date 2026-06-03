# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： 冯成
@File ： 02LangChain流式输出结果.py
@IDE ： PyCharm
"""
from langchain_community.llms.tongyi import Tongyi

# 不用qwen3-max，因为qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")

# 调用invoke向模型提问
res = model.stream(input= "你是谁呀，能做什么？")

for chunk in res:
    print(chunk, end=" ", flush=True)



