# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 13JsonOutputParser.py
@IDE ： PyCharm
"""
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi

# 1、定义模型
model = ChatTongyi(model = 'qwen3-max')

# 2、定义第一次提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居是{lastname}, 刚生了一个{gender}孩子，请你帮忙起一个名字。并且严格返回json格式的输出，key是name"
)

# 3、定义第二题提示词模板
second_prompt = PromptTemplate.from_template(
    "请你解释一下这个名字{name}的含义"
)

# 4、定义输出的类型
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# ============= 方法一，在最后大模型输出的消息格式为AIMessages，通过StrOutputParser 转换为字符串，这样最后可以直接打印 =======
# # 5、定义链的顺序，第一次输出AIMessage类型，通过Json输出转换为json格式(dict 字典输出)再送入模型，最后转换为字符串类型str
# chain = first_prompt | model | json_parser | second_prompt | model | str_parser
#
# # 6、调用链式开始
# # res = chain.invoke({"lastname": "冯四", "gender": "女"})
# # print(res)
#
# # 还可以流式输出结果
# for chunk in chain.stream({"lastname": "冯四", "gender": "女"}):
#     print(chunk, end="", flush=True)


# ============= 方法二，在最后大模型输出的消息格式为AIMessages不用处理，在最后打印输出的时候，调用.content进行文本输出即可 =======
# 5、定义链的顺序，第一次输出AIMessage类型，通过Json输出转换为json格式(dict 字典输出)再送入模型，最后转换为字符串类型str
chain = first_prompt | model | json_parser | second_prompt | model

# 6、调用链式开始
# res = chain.invoke({"lastname": "冯四", "gender": "女"})
# print(res)

# 还可以流式输出结果
for chunk in chain.stream({"lastname": "冯四", "gender": "女"}):
    print(chunk.content, end="", flush=True)
    print(type(chunk))