# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/28
@Auth ： fc
@File ： 02OpenAI库的基础使用.py
@IDE ： PyCharm
"""
from openai import OpenAI

# 1、获取client对象，OpenAI类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2、调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个助手并且不说废话"},
        {"role": "assistant", "content": "好的，我是编程专家并且话不多，你要问什么"},
        {"role": "user", "content": "输出1-10的数字，用python代码实现"}
    ]
)

# 3、处理结果
print(response.choices[0].message.content)