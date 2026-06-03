# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/29
@Auth ： 冯成
@File ： 06Json的基础使用.py
@IDE ： PyCharm
"""
import json

# 创建一个字典
d = {
    "name": "周杰伦",
    "age": "38",
    "gender": "男"
}

# python字典 -> 转换为JSON对象
json_key = json.dumps(d, ensure_ascii=False)
print(json_key)

list = [
    {
        "name": "周杰伦",
        "age": "38",
        "gender": "男"
    },

    {
        "name": "冯成",
        "age": "26",
        "gender": "男"
    },

    {
        "name": "王露露",
        "age": "26",
        "gender": "女"
    }
]
# 创建一个json数组，将python字典形式转换为json数组
print(json.dumps(list, ensure_ascii=False))

json_array_str = json.dumps(list, ensure_ascii=False)

print(json.loads(json_key), type(json.loads(json_key)))
print(json.loads(json_array_str), type(json.loads(json_array_str)))