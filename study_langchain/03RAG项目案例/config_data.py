# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/7
@Auth ： 冯成
@File ： config_data.py
@IDE ： PyCharm
"""
md5_path = "./md5.text"

# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"

# spliter
chunk_size = 1000
chunk_overlap = 100
separators =  ["\n\n", "\n", "。", "，", "！", "？"]
max_split_char_number = 1000   # 文本分割的阈值

# 相似度检索
similarity_threshold = 2  # 检索返回匹配的文档数量