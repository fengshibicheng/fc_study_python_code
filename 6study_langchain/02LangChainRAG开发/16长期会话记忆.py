# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 16长期会话记忆.py
@IDE ： PyCharm
"""
import json, os
from typing import Sequence
from langchain_core.messages import messages_from_dict, message_to_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory

# messages_from_dict  完成的是[字典，字典，字典] -> [消息，消息，消息]
# message_to_dict  完成的是单个message实例化的类（BaseMessage类字典） -> 转换为字典 dict  单个转单个
# AIMessage、HummanMessage、SystemMessage 都是BaseMessage的子类

class FileChatMessageHistory(BaseChatMessageHistory):

    def __init__(self, session_id, storage_path):
        self.session_id = session_id  # 会话id
        self.storage_id = storage_path  # 不同会话id的历史聊天记录，所储存的文件夹地址
        # 储存的文件地址
        self.store_id = os.path.join(self.storage_id, self.session_id)
        # 确保文件保存地址存在
        os.makedirs(os.path.dirname(self.store_id), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # Sequence序列  类似于元组，列表，tuple。list这样 的序列
        all_message = list(self.messages)   # 已有的消息列表
        all_message.extend(messages)    # 新的和已有的完成消息列表  extend是追加messages的多个消息。append只能追加单个消息

        new_message = [message_to_dict(message) for message in all_message]  # 列表推导式

        # 将消息字典转换为json数组保存到给定地址中
        # # 将数据写入文件，打开操作，写入操作
        # file_path = os.path.join(self.storage_id, self.session_id)
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # with open(file_path, 'w', encoding='utf-8') as f:
        with open(self.store_id, 'w', encoding='utf-8') as f:
            json.dump(new_message, f)

    def clear(self) -> None:
        # file_path = os.path.join(self.storage_id, self.session_id)
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # with open(file_path, 'w', encoding='utf-8') as f:
        with open(self.store_id, 'w', encoding='utf-8') as f:
            json.dump([], f)

    @property  # 通过@property装饰器方法，将messages函数变成成员属性
    def messages(self) -> list[BaseMessage]:
        try:
            with open(os.path.join(self.storage_id, self.session_id), 'r', encoding='utf-8') as f:
                message_data = json.load(f)  # 返回值里面都是字典
                return messages_from_dict(message_data)  # 将字典list转换为消息messages类型
        except FileNotFoundError:
            return []

def print_prompt(prompt):
    print("="*20, prompt.to_string(), "="*20)
    return prompt

def get_history(session_id):
    return FileChatMessageHistory(session_id, storage_path='./filechatmessages')

from langchain_community.chat_models.tongyi import  ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory

# 1、 定义一个模型
model = ChatTongyi(model = "qwen3-max")

# 2、提示词构成 方法一
# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史，回复用户的问题，对话历史{chat_history}, 用户提问{input}, 请回答"
# )
# 2、提示词构成 方法二
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史，回复用户的问题"),
        MessagesPlaceholder("history"),
        ("human", "请你回答如下问题 {input}")
    ]
)

# 3、输出类型转换
str_parser = StrOutputParser()

# 4、基本链路
base_chain = prompt | print_prompt | model | str_parser

store = {}  # 定义每个用户历史记录的字典，key就是session，value就是InMemoryChatMessageHistory类对象

# 5、创建一个新的链，增强原有链，自动附加消息  包装带历史记忆的链
conversion = RunnableWithMessageHistory(
    base_chain,  # 增强前的基本链路
    get_history,  # 通过会话ID获取InMemroyChatMessageHistory类对象
    input_messages_key="input",             # 表示用户在输入模版中的占位符
    history_messages_key="history"     # 表示用户在输入模版中的占位符
)

if __name__ == "__main__":

    # 固定格式，添加LangChain的配置，为当前配置的所属的session_id
    session_id = {
        "configurable":{
            "session_id": "user_001"
        }
    }

    # res = conversion.invoke({"input": "小明有2只猫"}, session_id)
    # print("第一次提问信息：", res)
    #
    # res = conversion.invoke({"input": "小花有1只猫"}, session_id)
    # print("第二次提问信息：", res)

    res = conversion.invoke({"input": "一共有几只猫"}, session_id)
    print("第三次提问信息：", res)