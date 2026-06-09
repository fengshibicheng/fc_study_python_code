# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/9
@Auth ： 冯成
@File ： rag.py
@IDE ： PyCharm
"""
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from file_history_store import get_history
from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi


def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)

    return prompt

def format_document(docs: list[Document]):
        if not docs:
            return "无相关参考资料"

        formatted_str = ""
        for doc in docs:
            formatted_str += f"文档片段：{doc.page_content}\n 文档元数据：{doc.metadata}\n\n"

        return formatted_str

def format_for_retriever(value: dict)->str:

    return value["input"]

def format_for_prompt_template(value):
    # {input, context, history}
    new_value = {}
    new_value["input"] = value["input"]["input"]
    new_value["context"] = value["context"]
    new_value["history"] = value["input"]["history"]
    return new_value


class RagService(object):
    def __init__(self):

        # 向量存储
        self.vector_service = VectorStoreService(
            embedding=DashScopeEmbeddings(model=config.embedding_model_name)
        )

        # 提示词模版
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "以我提供的已知参考资料为主，"
                 "简洁和专业的回答用户问题。参考资料:{context}。"),
                ("system", "并且我提供用户的对话历史记录，如下："),
                MessagesPlaceholder("history"),
                ("user", "请回答用户提问：{input}")
            ]
        )

        # 聊天模型
        self.chat_model = ChatTongyi(model=config.chat_model_name, streaming = True)

        # 链
        self.chain = self.__get_chain()

    # 私有的成员方法
    def __get_chain(self):
        """获取最终的执行链"""

        # 检索器对象
        retriever = self.vector_service.get_retriever()

        # 初始链
        chain = (
            {
                "input": RunnablePassthrough(),
                "context": RunnableLambda(format_for_retriever) | retriever | format_document
            }| RunnableLambda(format_for_prompt_template) |self.prompt_template | print_prompt |self.chat_model | StrOutputParser()
        )

        # 对话的历史记录保存
        conversation_chain = RunnableWithMessageHistory(       # 增强的链
            chain,   # 被增强的普通链
            get_history,  # 调用历史记忆
            input_messages_key="input",  # 用户输入的变量是什么
            history_messages_key="history",   # 历史消息的占位
        )

        return conversation_chain


if __name__ == '__main__':
    # session id 配置
    session_config ={
        "configurable":{
            "session_id":"user_001",
        }
    }
    res = RagService().chain.invoke({"input":"我身高160，应该穿什么尺码"}, session_config)
    print(res)