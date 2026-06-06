# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/1
@Auth ： 冯成
@File ： 07FewShot提示词模板.py
@IDE ： PyCharm
"""
# PromptTemplate 通用提示词模版
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate, ChatPromptTemplate

# 1、通用提示词 示例的模板
example_template = PromptTemplate.from_template("单词： {word}, 反义词：{antonym}")

# 示例数据的动态数据注入，要求是list内部套字典
example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]

few_shot_template = FewShotPromptTemplate(
    example_prompt = example_template,    # 示例数据的模板
    examples = example_data,        # 示例的数据（用来注入动态数据的），list内嵌字典
    prefix = "告知我单词的反义词，我提供如下的示例：",          # 示例之前的提示词    前缀
    suffix = "基于前面的示例告知我，{input_word}的反义词是？",          # 示例之后的提示词  后缀
    input_variables=['input_word']      # 声明在前缀或后缀中所需要注入的变量名
)

# 实例化提问输出
prompt_text = few_shot_template.invoke(input = {"input_word": "东"}).to_string()
print(prompt_text)


model = Tongyi(mode = "qwen-max")
res = model.invoke(input = prompt_text)

print(res)