# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/3
@Auth ： 冯成
@File ： 21内存向量存储.py
@IDE ： PyCharm
"""
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding = DashScopeEmbeddings()
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source"  # 指定本条数据来源是哪里
)

document = loader.load()


# id1, id2, id3.....
# 向量存储的新增，删除，检索
vector_store.add_documents(
    documents=document,   # 被添加的文档。list[Document]
    ids= ["id"+str(i) for i in range(1, len(document)+1)]  # 给添加的文档提供字符串id list[str]
)

# 向量删除的id索引
vector_store.delete(
    ["id1", "id2"]
)

# 检索 返回类型list[Document]
result = vector_store.similarity_search(query="python语法是不是好学", k=3)

print(result)