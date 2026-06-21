# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/4
@Auth ： fc
@File ： 24RunnablePassthrough的使用.py
@IDE ： PyCharm
"""
"""
提示词：用户的提问 + 向量库中检索到的参考资料

向量存储的实例，通过add_texts(list[str)方法 可以快速添加到向量存储中。
  流程：
    1、先通过向量存储检索匹配信息
    2、将用户提问和匹配信息一同封装到提示词模板中提问模型
*****************************************************************************
retriever:
    - 输入：用户的提问    str
    - 输出：向量库的检索结果  list[Document]
prompt:
    - 输入：用户的提问 + 向量库的检索结果  dict
    - 输出：完整的提示词                PromptValue
*****************************************************************************
23 向量检索构建提示词.py（链一） 和 24 RunnablePassthrough的使用的区别（链二）
场景  	    |  手动传 context (你的链一)	 |  retriever 自动生成 (链二)
检索在哪	    |  链条外部，自己写查询代码	     |    链条内部，框架自动检索
invoke 传参	|  必须手动构造context字段	     |  只需要传input，context 自动生成
批量 / 接口	|  每次调用前都要手动查文档，冗余	 |  封装完毕，调用即自动查，适合接口项目
*****************************************************************************
手动传 context：
    临时调试、自定义特殊检索逻辑、自己控制检索规则
retriever 链条：    
    正式 RAG 项目、接口部署、大批量问答，少写重复代码
"""
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings.dashscope import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)
    return prompt

"""
    前置工作，初始化 内存中的向量存储 实例, 将用户提问在知识库中余弦相似度检索出top-k，再转换为预处理为列表格式
"""
# 1、向量存储，在内存中存储
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

# 2、准备资料，向量存储（向量库的数据）
# add_texts 传入一个 list[str]
vector_store.add_texts(
    ["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"]
)

# 3、langchain中向量存储对象，有一个方法：as_retriever，可以返回一个Runnable接口的子类实例对象
retriever = vector_store.as_retriever(search_kwargs = {"k": 2})

# 4、输出转换为字符串
def format_func(docs):
    """
    def format_func(docs: list[Document]) -> str
    """
    if not docs:
        return "无相关参考资料"

    # 方法一
    # formatted_str = "["
    # for doc in docs:
    #     formatted_str += doc.page_content
    # formatted_str += "]"

    # 方法二
    doc_page_content = [doc.page_content for doc in docs]
    formatted_str = "[" + "\t".join(doc_page_content) + "]"

    return formatted_str

# 5、通过调用 runnablelambda 包装自定义函数为 Runnable类
format_runnable = RunnableLambda(format_func)

# ============================================= 正式开始 ===========================================
# 1、创建聊天模型
model = ChatTongyi(model = "qwen3-max")

# 2、提示词模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}。"),
        ("user", "用户提问：{input}")
    ]
)

# 3、构造 chain
chain = {"input": RunnablePassthrough(),  # RunnablePassthrough 用户原问题原样保留， 相当于【用户输入的占位符】
         "context": retriever | format_runnable} | prompt | print_prompt | model | StrOutputParser()

input_text = "怎么减肥？"
result = chain.invoke(input_text)

print(result)