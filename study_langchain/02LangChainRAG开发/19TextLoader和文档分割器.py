# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/3
@Auth ： 冯成
@File ： 19TextLoader和文档分割器.py
@IDE ： PyCharm
"""
"""
TextLoader 是一个简单的加载器，可以加载文本文件内容，返回仅有一个Document对象的list

RecursiveCharacterTextSplitter递归字符文本分割器，是LangChain官方推荐的默认分割器
    *基于文本的自然段落分割大文档为小文档
    *可以指定小文档的最大字符数、重叠字符数
    *可以手动指定段落划分的依据（符号）以及字符数量统计函数
"""
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # 递归文档分割器

loader = TextLoader(
    file_path="./data/python基础语法.txt",
    encoding="utf-8"
)

docs = loader.load()       # [Document]

spliter = RecursiveCharacterTextSplitter(
    chunk_size=200, # 分段得到最大字符数
    chunk_overlap=20,  # 分段之间允许重叠的字符串
    # 文本自然段落分割的依据符号
    separators=["\n\n", "\n", "。", "，", ",", "!", "?", " ", ""],
    length_function=len,   # 统计字符的依据函数
)

split_doc = spliter.split_documents(documents=docs)
print(len(split_doc))
for doc in split_doc:
    print("***"*20)
    print(doc)
    print("***"*20)