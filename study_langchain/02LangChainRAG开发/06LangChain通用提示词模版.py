# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： 冯成
@File ： 06LangChain通用提示词模版.py
@IDE ： PyCharm
"""
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi


prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)
# 调用.format方法注入即可
prompt_text = prompt_template.format(lastname="张", gender='女儿')
# print(prompt_text)

model = Tongyi(model = "qwen-max")
# res = model.invoke(input=prompt_text)
#
# for chunk in res:
#     print(chunk, end="", flush=True)

chain = prompt_template | model

chain.invoke(input={"lastname": "冯", "gender": "男士"})

print(chain.invoke(input={"lastname": "冯", "gender": "男士"}))
