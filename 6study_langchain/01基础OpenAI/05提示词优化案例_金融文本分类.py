# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/29
@Auth ： fc
@File ： 05提示词优化案例_金融文本分类.py
@IDE ： PyCharm
"""
from openai import OpenAI

# 1、创建模型
client = OpenAI(
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
)

# 2、调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个金融行业的专家，只能从【市场行情、理财推荐、风险警示、政策解读、业务咨询、无关内容】中选择一个类别，直接输出分类结果，不要额外解释。 下面有示例"},

        {"role": "user",   "content": "今日央行公告宣布降....."},
        {"role": "assistant", "content": "政策解读"},
    ],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content)