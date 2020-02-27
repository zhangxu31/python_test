#coding=utf8
import os
#import tkFileDialog
    
def readFilename(file_dir):
    for root, dirs, files in os.walk(file_dir): 
        return files,dirs,root
 
def findstring(pathfile):
    fp = open(pathfile, "r",encoding='UTF-8')#注意这里的打开文件编码方式
    strr = fp.read()
    #print strr.find("DoubleVec")
    if(strr.find("console.log") != -1):
        #print ('here?')
        return True
    return False
    
def startfind(files,dirs,root):
    for ii in files:
        #print(ii)
        #if ii.endswith('.lua'):
        try:
            if(findstring(root+"/"+ii)):
                result.add(root+"/"+ii)
                #print (root+"/"+ii)
        except Exception as err:
            print(err)
            continue
            
                
    for jj in dirs:
        fi,di,ro = readFilename(root+"/"+jj)
        startfind(fi,di,ro)
    
if __name__ == '__main__':
    default_dir = "/Users/zhangxu/work/CCDC/trunk"  # 设置默认打开目录
    #file_path = default_dir #th.expanduser(default_dir)))
    res_file = open("result.txt", "w")
    result = set()
    files,dirs,root = readFilename(default_dir)
    startfind(files,dirs,root)
    for s in result:
        res_file.write(s + "\n")
