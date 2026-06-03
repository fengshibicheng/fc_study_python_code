# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/29
@Auth ： 冯成
@File ： 01LangChain访问阿里通义千问大模型.py
@IDE ： PyCharm
"""
from langchain_community.llms.tongyi import Tongyi

# 不用qwen3-max，因为qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")

# 调用invoke提问大模型
res = model.invoke(input="你是谁呀，能做什么")

print(res)