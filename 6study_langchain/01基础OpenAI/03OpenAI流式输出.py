# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/29
@Auth ： 冯成
@File ： 03OpenAI流式输出.py
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
    ],
    stream=True  # 开启流式输出模式，就是一个字一个字蹦出来的样子，这样会显示思考的过程。
)

# 3、处理结果
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content,
              end=' ',     # 段落之间进行空行, 用空格连接文字
              flush=True)   # 立刻刷新缓冲区


