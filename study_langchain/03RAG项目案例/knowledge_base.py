# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/7
@Auth ： 冯成
@File ： app_file_up.py
@IDE ： PyCharm
"""
import os
import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime


def check_md5(md5_str: str):
    """
    return  False(md5未处理过) True(已经处理过，已有记录)
    """
    if not os.path.exists(config.md5_path):
        # if 进入表示文件不存在，那肯定没有处理过这个md5了
        open(config.md5_path, "w", encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, "r", encoding="utf-8").readlines():
            line = line.strip()     # 处理字符串前后的空格和回车
            if line == md5_str:
                return True     # 已处理过
        return False

def save_md5(md5_str: str):
    """ 将传入的md5字符串，记录到文件内保存"""
    with open(config.md5_path, "a", encoding="utf-8") as f:
        f.write(md5_str + '\n')

def get_string_md5(input_str: str, encoding='utf-8'):
    """将传入的字符串转换为md5字符串"""
    # 将字符串转换为bytes字节数组
    str_bytes = input_str.encode(encoding=encoding)
    # 创建md5对象
    md5_obj = hashlib.md5()    # 得到md5对象
    md5_obj.update(str_bytes)   # 更新内容（传入即将要转换的字节数组）
    md5_hex = md5_obj.hexdigest()  # 得到md5的十六进制字符串

    return md5_hex

class KnowledgeBaseService(object):

    def __init__(self):
        # os.makedirs 表示如果该文件夹不存在，则会创建一个文件夹；如果存在则跳过
        os.makedirs(config.persist_directory, exist_ok=True)

        # 一、创建文本分割器的对象
        self.spliter=RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,       # 分段得到的最大文本数量
            chunk_overlap=config.chunk_overlap,    # 相邻两段之间允许重叠的文本数量
            separators=config.separators,       # 文本划分的标准，比如。 ， ！ ？ 这样的字符
            length_function=len     # 用python自带的统计长度的函数len作为统计文本长度的依据
        )

        # 二、创建向量存储的实例 Chroma 向量库对象
        self.chroma=Chroma(
            collection_name=config.collection_name,     # 数据库的表名，一般会放到配置文件当中，方便修改
            persist_directory=config.persist_directory,  # 数据库本地存储文件夹
            embedding_function=DashScopeEmbeddings(
            model=config.embedding_model_name,    # 默认是v1，改成v4比较新，效果更好
            ),
        )

    def upload_by_str(self, data: str, filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        # 先得到传入字符串的md5值
        md5_hex = get_string_md5(data)

        if check_md5(md5_hex):
            return "[跳过]传入文本已经存在向量库中"

        # 文本分片
        if len(data) > config.max_split_char_number:
            knowledge_chunk: list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunk = [data]

        metadata = {
            "source" : filename,
            # 我们习惯的时间格式是 2026-06-08 10:00：00
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "小冯",
        }

        print("开始写入向量库...")
        # 写入向量库
        self.chroma.add_texts(    # 内容就加载到向量库中了
            # iterable -> list \ tuple
            texts = knowledge_chunk,
            metadatas=[metadata] * len(knowledge_chunk)
        )

        # 保存md5
        save_md5(md5_hex)

        return "[成功]内容已经成功载入向量库"

if __name__ == "__main__":
    service = KnowledgeBaseService()
    r = service.upload_by_str("周杰轮", 'testfile')
    print(r)

