# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/4
@Auth ： 冯成
@File ： 24RunnablePassthrough的使用.py
@IDE ： PyCharm
"""
"""
提示词：用户的提问 + 向量库中检索到的参考资料

向量存储的实例，通过add_texts(list[str)方法 可以快速添加到向量存储中。
  流程：
    1、先通过向量存储检索匹配信息
    2、将用户提问和匹配信息一同封装到提示词模板中提问模型
"""
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1、创建聊天模型
model = ChatTongyi(model = "qwen3-max")

# 2、提示词模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}。"),
        ("user", "用户提问：{input}")
    ]
)

# 3、向量存储，在内存中存储
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

# 4、准备资料，向量存储（向量库的数据）
# add_texts 传入一个 list[str]
vector_store.add_texts(
    ["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"]
)

input_text = "怎么减肥？"

# langchain中向量存储对象，有一个方法：as_retriever，可以返回一个Runnable接口的子类实例对象
retriever = vector_store.as_retriever(search_kwargs = {"k": 2})

def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)
    return prompt

# def format_func(docs: list[Document]) -> str:
def format_func(docs):
    if not docs:
        return "无相关参考资料"

    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str += "]"

    return formatted_str

# 包装自定义函数为Runnable
format_runnable = RunnableLambda(format_func)

# chain
chain = (
    {"input": RunnablePassthrough(), "context": retriever | format_runnable} | prompt | print_prompt | model | StrOutputParser()
)

result = chain.invoke(input_text)
print(result)
"""
retriever:
    - 输入：用户的提问    str
    - 输出：向量库的检索结果  list[Document]
prompt:
    - 输入：用户的提问 + 向量库的检索结果  dict
    - 输出：完整的提示词                PromptValue
"""