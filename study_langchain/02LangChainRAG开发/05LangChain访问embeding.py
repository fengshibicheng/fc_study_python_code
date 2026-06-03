# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： 冯成
@File ： 05LangChain访问embeding.py
@IDE ： PyCharm
"""
# DashScope 达摩院
from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings()

print(model.embed_query("我是冯成"))

print(model.embed_documents(["我是冯成", "这是一个实验"]))