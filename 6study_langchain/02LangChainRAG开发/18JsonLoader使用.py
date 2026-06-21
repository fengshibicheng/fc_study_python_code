# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/3
@Auth ： fc
@File ： 18JsonLoader使用.py
@IDE ： PyCharm
"""
#=========================================================
"""
JSONLoader 依赖jq库，通过pip install jq 进行安装
    .表示根、[]表示数组
    .name 表用从根取name的值
    .hobby[1]表示取hobby对应数组的第二个元素
    .[]表示将数组内的每个字典（JSON对象）都取到
    .[].name表示取数组内的每个字典（JSON）对象的name对应的值
JSONLoader初始化有4个主要参数：
    file_path: 文件路径，必填
    jq_schema: jq解析语法，必填
    text_content: 抽取到的是否是字符串，默认True，非必填
    json_lines: 是否是JsonLines文件，默认False，非必填
jsonlines文件：每一行都是一个独立的字典（Json对象）
"""
#=========================================================

from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./data/stu.json",
    jq_schema=".other.addr",
)

loader1 = JSONLoader(
    file_path="./data/stus.json",
    jq_schema=".[].name",
    text_content=False,  # 默认是字符串，如果抽的不是字符串，而是整个json字典的话，这里需要修改为False
)

loader2 = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,  # 默认是字符串，如果抽的不是字符串，而是整个json字典的话，这里需要修改为False
    json_lines= True, # 告知JSONLoader 这是一个JSONLines文件（每一行都是一个独立的标准JSON）
)

# 消息加载方式有.load() 以及懒加载 .lazy_load()
document = loader1.load()
print(document[0].metadata)
print(document)