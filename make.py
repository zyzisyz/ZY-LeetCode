# coding=utf-8
# 这是一个用于爬取Leetcode网页
# 并自动创建刷题md文档的python脚本

import requests
import os
from bs4 import BeautifulSoup

# url
Leetcode_CN_Url = "https://leetcode-cn.com/problemset/all/"
Leetcode_Url = "https://leetcode.com/problemset/all/"
MyGithub_Url = "https://github.com/zyzisyz/ZY-LeetCode/blob/master/LeetCode/"

# Path
Current_Path = os.path.abspath('.')
LeetCode_Path = Current_Path+"/LeetCode/"


# 修改num格式
def NumToString(num):
    if(num < 10):
        return "00"+str(num)
    elif(num < 100):
        return "0"+str(num)
    else:
        return str(num)


# 爬取题目
def GetProblem(num, url):
    pass


# 创建md文档
def MakeMD(num):
    num = int(num)
    a = ""
    if not os.path.exists(LeetCode_Path+NumToString(num)):
        os.mkdir(LeetCode_Path+NumToString(num))
        print("未找到"+NumToString(num)+"文件夹，" +
              "已经成功创建了"+NumToString(num)+"文件夹...")
    else:
        print(NumToString(num) + "文件夹已经存在...")


# 修改README.md
def Update_RDM(num):
    pass


# 主函数
def main():
    os.system("cls")
    print("start!")

    print("\n\nmake complete!")


main()
