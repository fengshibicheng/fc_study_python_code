# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 08模版类的format和invoke方法对比.py
@IDE ： PyCharm
"""
# 从langchain核心包core中导入三个常用的提示词模板
from langchain_core.prompts import PromptTemplate            # 通用提示词模版     支持动态注入信息【一般是一条】
from langchain_core.prompts import FewShotPromptTemplate    # FewShot提示词模版  支持基于模板 注入【任意数量的示例信息】
from langchain_core.prompts import ChatPromptTemplate       # Chat提示词模版     支持注入【任意数量的历史会话信息】

"""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable ->Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable ->Runnable
ChatPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate -> RunnableSerializable ->Runnable
"""

template = PromptTemplate.from_template("我叫{lastname}, 最喜欢的运动是{sport}")

# format 函数传入的是 k = v 这样的形式
res = template.format(lastname="张三", sport="跑步")
print(res, type(res))

# invoke 函数传入的是 字典的形式 {"k": "v"}
res1 = template.invoke(input = {"lastname": "李四", "sport": "打乒乓球"})
print(res1.text, type(res1))

res2 = template.invoke({"lastname": "李四", "sport": "打乒乓球"}).to_string()
print(res2, type(res2))