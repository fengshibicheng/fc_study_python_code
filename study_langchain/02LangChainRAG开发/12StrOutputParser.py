# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 12StrOutputParser.py
@IDE ： PyCharm
"""
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model = 'qwen3-max')
prompt =  PromptTemplate.from_template(
    "我的邻居姓{lastname}， 刚生了{gender}孩，请你帮我起一个名字，进告知名字，无需告诉其他的"
)

parser = StrOutputParser()
# chain = prompt | model | StrOutputParser | model
chain = prompt | model  | parser | model

res = chain.invoke({"lastname": "张三", "gender": "男"})
print(res.content)

# chain = prompt | model  | parser | model |parser
# res = chain.invoke({"lastname": "张三", "gender": "男"})
# print(res)