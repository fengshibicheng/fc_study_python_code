# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/9
@Auth ： fc
@File ： app_qa.py
@IDE ： PyCharm
"""
import streamlit as  st
from rag import RagService
import config_data as config
import time
"""
    基于streamlit框架实现的web网页，运行方式，在对应的项目文件目录中输入：streamlit run app_qa.py
"""

# 标题
st.title("智能客服")

# 分隔符--------
st.divider()

# 避免性能压力，session_state是一个字典 存入对象
if "message" not in st.session_state:
    st.session_state["message"]=[{"role": "assistant", "content": "你好，有什么可以帮助你？"}]

if "rag" not in st.session_state:
    st.session_state["rag"]= RagService()

#循环 输出历史信息，原本只记录但页面不显示
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 在页面最下方提供用户输入栏
prompt= st.chat_input()

if prompt :
    # 在页面输出用户的提问
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    ai_res_list= []
    with st.spinner("AI 思考中......."):
        # 调用 RAG服务

        # 方法一、直接输出
        # res= st.session_state["rag"].chain.invoke({"input":prompt},config.session_config)
        #
        # st.chat_message("assistant").write(res)
        # st.session_state["message"].append({"role":"assistant","content":res})

        # 方法二、流式输出
        res_stream = st.session_state["rag"].chain.stream({"input": prompt}, config.session_config)

        #  添加一个捕获器，这样可以原样不动的进来，原样不动的出去，中间还会 构造一个 list=[] 来记录结果，方便保存展示到页面当中
        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(res_stream, ai_res_list))
        st.session_state["message"].append({"role": "assistant", "content": "".join(ai_res_list)})
                                                                         # “”.join功能： eg：['a', 'b', 'c', 'd']  -> abcd
                                                                         # “-”.join功能： eg：['a', 'b', 'c', 'd']  -> a-b-c-d