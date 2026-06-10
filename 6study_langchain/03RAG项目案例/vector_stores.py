# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/8
@Auth ： 冯成
@File ： vector_stores.py
@IDE ： PyCharm
"""
"""
    基于 Chroma 向量库 + 阿里通义嵌入模型的知识库检索服务，核心功能：把【用户提问文本】转为向量、根据问题语义相似度检索知识库内容并返回。
"""
from langchain_chroma import Chroma
import config_data as config

class VectorStoreService(object):
    def __init__(self, embedding):
        """
        embedding: 嵌入模型的传入
        """
        self.embedding = embedding  # 私有成员变量

        # 一、创建向量数据库类实例。
        # 在knowledge_base.py文件中的向量类实例作用是： 为了将输入的知识库文本转换为向量类；
        # 在这里再创建向量类作用：是把用户输入转换为向量类
        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        """返回向量检索器，方便加入chain"""
        return self.vector_store.as_retriever(
            search_kwargs = {
                "k": config.similarity_threshold   #每次检索应该返回几个结果
            }
        )

if __name__ == "__main__":
    from langchain_community.embeddings import  DashScopeEmbeddings
    # retriever 检索器
    retriever = VectorStoreService(DashScopeEmbeddings(model = config.embedding_model_name)).get_retriever()

    res = retriever.invoke("我的体重180斤，尺码推荐")
    print(res)
    for r in res:
        print(r.page_content)