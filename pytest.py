# coding=utf-8
# 测试通过
import os
 
mypath = "/Users/zhangxu/work/python-learning"
 
"""
其中最下面的if语句为测试代码部分，当输入'123'时，会打印当前目录和当前目录的所有子目录下包含'123'的所有文件
当输入'.jpg'时，会打印当前目录和当前目录的所有子目录下包含'.jpg'格式的的所有文件
当输入'.'时，会打印当前目录和当前目录的所有子目录下 的所有文件
"""
 
 
def search(a, b):#a为路径，b为关键词
    for file in os.listdir(a):
        if os.path.isfile(a + '/' + file):
            if b in file:
                print(file, '==>', a + '/' + file)
        else:
            search(a + '/' + file, b)
 
 
if __name__ == "__main__":
    search(os.path.abspath(mypath), '123') #jpg格式查找 #'.'全部文件  '123'