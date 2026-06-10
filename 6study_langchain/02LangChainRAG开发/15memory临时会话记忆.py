# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 15memory临时会话记忆.py
@IDE ： PyCharm
"""
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser, JsonOutputParse
# 导入一个临时会话记忆的包
from langchain_core.runnables.history import RunnableWithMessageHistory  # 记忆绑定包装器
from langchain_core.chat_history import InMemoryChatMessageHistory  # 专门用来存放一轮轮的用户 / AI 对话消息，程序运行时有效，重启 / 关闭程序数据就清空（非持久化）。

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


def print_prompt(prompt):
    print("="*20, prompt.to_string(), "="*20)
    return prompt

# 3、输出类型转换
str_parser = StrOutputParser()
json_parser = JsonOutputParse()

# 4、基本链路
base_chain = prompt | print_prompt | model | str_parser

store = {}  # 定义每个用户历史记录的字典，key就是session，value就是InMemoryChatMessageHistory类对象

def get_history(session_id):
    """
    实现通过session_id来获取InMemoryChatMessageHistory类对象
    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

# 5、创建一个新的链，增强原有链，自动附加消息  包装带历史记忆的链
conversion = RunnableWithMessageHistory(
    base_chain,  # 增强前的基本链路
    get_history,  # 通过会话ID获取InMemroyChatMessageHistory类对象
    input_messages_key="input",             # 表示用户在输入模版中的占位符
    history_messages_key="history"     # 表示用户在输入模版中的占位符变量名
)

if __name__ == "__main__":

    # 固定格式，添加LangChain的配置，为当前配置的所属的session_id
    session_id = {
        "configurable":{      # 第一层：固定key，LangChain识别配置区
            "session_id": "user_001"    # 第二层：真正存用户编号
        }
    }

    res = conversion.invoke({"input": "小明有2只猫"}, config = session_id)
    print("第一次提问信息：", res)

    res = conversion.invoke({"input": "小花有1只猫"}, config = session_id)
    print("第二次提问信息：", res)

    res = conversion.invoke({"input": "一共有几只猫"}, config = session_id)
    print("第三次提问信息：", res)
