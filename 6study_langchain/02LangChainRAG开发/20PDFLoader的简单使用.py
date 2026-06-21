# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/3
@Auth ： fc
@File ： 20PDFLoader的简单使用.py
@IDE ： PyCharm
"""
from langchain_community.document_loaders import PyPDFLoader

pdf_loader = PyPDFLoader(
    file_path="./data/pdf1.pdf",
    mode="page"  # 默认是page模式，每一页面形成一个Document文档对象；可选single模式，无论多少页面，都形成一个页面Document返回
        # "single" 模式
)

pdf_loader2 = PyPDFLoader(
    file_path="./data/pdf2.pdf",
    password="itheima"
)

i = 0
for doc in pdf_loader2.lazy_load():
    i +=1
    print(doc)
    print("="*20, i)