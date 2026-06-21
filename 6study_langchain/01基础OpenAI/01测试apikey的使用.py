# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/28
@Auth ： fc
@File ： 01测试apikey的使用.py
@IDE ： PyCharm
"""
import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-math-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": "我是你的有用助手，可以帮你干很多事情"},
        {"role": "user", "content": "你是谁？"},
    ],
    stream=True
)
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)