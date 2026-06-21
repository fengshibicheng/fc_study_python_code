# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/4
@Auth ： fc
@File ： 23向量检索构建提示词.py
@IDE ： PyCharm
"""
"""
提示词：用户的提问 + 向量库中检索到的参考资料

向量存储的实例，通过add_texts(list[str)方法 可以快速添加到向量存储中。
  流程：
    1、先通过向量存储检索匹配信息
    2、将用户提问和匹配信息一同封装到提示词模板中提问模型
"""
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

# 3、user问题
input_text = "怎么减肥？"

# 4、检索向量库  相似度搜索
result = vector_store.similarity_search(input_text, k=2)

# 5、将检索结果进行预处理
# # 方法一，两个文本之间，没有分隔符
# reference_text = "["
# for doc in result:
#     reference_text += doc.page_content
# reference_text += "]"
# 方法二，文档之间用换行隔开，LLM更容易区分不同参考片段  "\t" 表示制表符； “\n” 表示换行符
contents = [doc.page_content for doc in result]
reference_text = "[" + "\t".join(contents) +"]"

# print(reference_text)

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
chain = prompt | print_prompt | model | StrOutputParser()

# 4、invoke调用 {"key": "value"}
res = chain.invoke({"input": input_text, "context": reference_text})

print(res)
