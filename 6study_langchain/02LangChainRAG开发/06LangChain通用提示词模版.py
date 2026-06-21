# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： fc
@File ： 06LangChain通用提示词模版.py
@IDE ： PyCharm
"""
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 1、创建通用提示词模版，用{}表示占位符
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)

# 2、实例化占位符，进行调用.format方法注入即可
prompt_text = prompt_template.format(lastname="张", gender='女儿')
# print(prompt_text)

#3、大模型实例化
model = Tongyi(model = "qwen-max")

# 3-1、常规的提问方式 invoke，以及回答
# res = model.invoke(input=prompt_text)
# for chunk in res:
#     print(chunk, end="", flush=True)

# 4、链式方式
chain = prompt_template | model

chain.invoke(input={"lastname": "冯", "gender": "男士"})

print(chain.invoke(input={"lastname": "冯", "gender": "男士"}))
