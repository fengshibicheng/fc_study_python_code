# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 14Runnablelambda函数的基础使用.py
@IDE ： PyCharm
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_community.chat_models.tongyi import ChatTongyi

# 1、定义模型
model = ChatTongyi(model = "qwen3-max")

# 2、作为两个模型中间的格式处理转换
str_parser = StrOutputParser()
json_parser = JsonOutputParser()
# 函数的入参是 AI message, 返回应该是 dict；   注意这里字典接收的信息应该是名字，要有.content
my_func = RunnableLambda(lambda ai_message: {"name": ai_message.content})

# 3、定义第一次提示词模板
first_prompt = PromptTemplate.from_template(
    "我有一个邻居刚生了一个小孩，叫{lastname}，是一个{gender}, 请你帮我起一个名字，只返回名字"
)

# 4、定义第二次提示词模版
second_prompt = PromptTemplate.from_template(
    "请你根据名字{name}，进行解释"
)

# 5、定义链路
chain = first_prompt | model | my_func | second_prompt | model | str_parser

str = chain.invoke({"lastname": "李四", "gender": "女孩"})
print(str)
