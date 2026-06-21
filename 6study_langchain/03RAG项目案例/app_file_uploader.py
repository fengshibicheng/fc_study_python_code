# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/6
@Auth ： fc
@File ： app_file_uploader.py
@IDE ： PyCharm
"""
"""
    基于streamlit框架实现的web网页，运行方式，在对应的项目文件目录中输入：streamlit run app_file_uploader.py
"""
# 基于Streamlit 完成WEB网页上传服务
# Streamlit特点：当WEB页面发生变化时，则代码重新执行一遍
import time
import streamlit as st
from knowledge_base import KnowledgeBaseService

# 添加网页标题
st.title("知识库更新服务")

# file_uploader
uploader_file = st.file_uploader(
    label = "请上传TXT文件",
    type = ['txt'],
    accept_multiple_files = False,  # False表示仅接受一个文件的上传
)

# session_state 就是一个字典
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()   # 实例化 knowledgebaseservice()

if uploader_file is not None:
    # 提取文件的信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024  # KB

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

    # get_value -> bytes -> decode('utf-8')
    text = uploader_file.getvalue().decode('utf-8')

    with st.spinner("载入知识库中...."):   # 在spinner内执行的代码执行过程中，会有一个转圈动画
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(data = text, filename = file_name)
        st.write(result)
