# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/3
@Auth ： 冯成
@File ： 22外部向量持久化存储.py
@IDE ： PyCharm
"""
"""
LangChain内提供向量存储功能，可以基于：
    *InMemoryVectorStore，完成内存向量存储
    *Chroma，外部数据库向量存储

向量存储类均提供3个通用API接口：
    *add_document, 添加文档到向量存储
    *delete, 从向量存储中删除文档
    *similarity_search: 相似度搜索
    
查询阶段（检索）
Query text ——> Embedding model ——转换> Query vector ——> Similarity Search ——匹配> Vector stores
"""
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings.dashscope import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader, JSONLoader, PyPDFLoader, TextLoader
from langchain_chroma import Chroma

# 1、内存中的数据向量化（不能永久保存）   方法一
# vector_store = InMemoryVectorStore(
#     embedding = DashScopeEmbeddings()
# )
# 1、外部数据向量化（调用外接向量库，可以永久保存）   方法二
vector_store = Chroma(
    collection_name="test", # 当前向量存储起个名字，类似数据库的表的名称
    embedding_function=DashScopeEmbeddings(), # 嵌入模型
    persist_directory="./chroma_db"   # 指定数据存储的文件夹
)

# 2、读取文本csv数据
loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source"  # 指定本条数据来源是哪里
)

document = loader.load()


# 3、向量存储的新增，删除，检索
# id1, id2, id3.....
# 向量存储的新增
vector_store.add_documents(
    documents=document,   # 被添加的文档。list[Document]
    ids= ["id"+str(i) for i in range(1, len(document)+1)]  # 给添加的文档提供字符串id list[str]
)

# 向量删除的id索引
vector_store.delete(
    ["id1", "id2"]
)

# 检索 返回类型list[Document]
result = vector_store.similarity_search(
    query="python语法是不是好学",
    k=1,  # 检索的结果要几个
    filter = {"source": "黑马程序员"},
)

print(result)