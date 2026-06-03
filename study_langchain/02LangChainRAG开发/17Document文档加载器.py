# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/3
@Auth ： 冯成
@File ： 17Document文档加载器.py
@IDE ： PyCharm
"""
from langchain_community.document_loaders import CSVLoader, JSONLoader, PDFPlumberLoader
# CSV loader 的使用
loader= CSVLoader(
    file_path = './data/stu.csv',
    csv_args={
        "delimiter": ",",   # 指定分隔符
        "quotechar": '"',  # 指定带有分割符文本的引号包围是单引号还是双引号
        # 如果数据原本有表头，就不需要fieldnames，如果有的话就不用加入filedname这个字典
        "fieldnames": ['a', 'b', 'c', 'd']
    },
    encoding='utf-8'   # window状态下，指定编码为utf-8
)

#=============方法一，适用内存大的方式===============================
# # 批量加载， .load() ->[Document, Document, ....]
# documents = loader.load()
#
# for document in documents:
#     print(type(document), document)

#=============方法二，适用内存小的时候一段一段加载===============================
# 懒加载 .lazy_load()  迭代器[Document]
for document in loader.lazy_load():
    print(document, type(document))
