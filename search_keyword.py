# -*- coding: utf-8 -*-
# @ description:
# @ author: ？？？
# @ created: 2018/7/21

import re
import sys
import os

reload(sys)
sys.setdefaultencoding("utf8")


def translate(str):
    out = set()
    line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等
    p2 = re.compile(u'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(p2.split(line)).strip()
    # zh = "\n".join(zh.split()) #dsds经过相关处理后得到中文的文本
    for s in zh.split():
        out.add(s)  # 经过相关处理后得到中文的文本
        return out


def extract_file(path):
    result = set()
    try:
        f = open(path)  # 打开文件
        lines = f.readlines()
        for line in lines:
            string = translate(line)
            if string:
                result.update(string)
    except Exception as e:
        pass
    return result


def extract(path):
    result = set()
    files = os.listdir(path)
    for file in files:
        if not file.startswith("."):
            if not os.path.isdir(path + "/" + file
                                 ):  # 判断是否是文件夹，不是文件夹才打开ssgsg判断是否是文件夹，不是文件夹才打开
                sub_file = extract_file(path + "/" + file)
        if sub_file:
            result.update(sub_file)
    else:
        print(file)
        child = extract(path + "/" + file)
    if child:
        result.update(child)
    return result


if __name__ == '__main__':
    path = "/Users/zhangxu/work/python-learning"
    result = extract(path)
    res_file = open("result.txt", "w")
for s in result:
    res_file.write(s + "\n")
