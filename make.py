# coding=utf-8
# 这是一个用于爬取Leetcode网页
# 并自动创建刷题md文档的python脚本

import requests
import os
from bs4 import BeautifulSoup
import sys

# MD_text
text = "# [num. ](url)\n\ndescribe\n\n## 我的思路\n\n## C++\n\n```cpp\n\n```"
text = text.encode('utf-8')


# url
Leetcode_CN_Url = "https://leetcode-cn.com/problemset/all/"
Leetcode_Url = "https://leetcode.com/problemset/all/"
MyGithub_Url = "https://github.com/zyzisyz/ZY-LeetCode/blob/master/LeetCode/"

# Path
Current_Path = os.path.abspath('.')
LeetCode_Path = Current_Path+"/LeetCode/"


# 修改num格式
def NumToString(num):
    num = int(num)
    if(num < 10):
        return "00"+str(num)
    elif(num < 100):
        return "0"+str(num)
    else:
        return str(num)


# 爬取题目
def GetProblem(num, url):
    pass


# 创建MD_text
def Make_MD_Text(num):
    num = int(num)
    num = NumToString(num)
    text = "# ["+num+". ](url)\n\n题目\n\n## 我的思路\n\n## C++\n\n```cpp\n\n```"
    return text


# 创建md文档
def Make_MD_File(num, text):
    num = int(num)
    num = NumToString(num)
    a = ""
    if not os.path.exists(LeetCode_Path+num):
        os.mkdir(LeetCode_Path+num)
        print("未找到"+num+"文件夹，" +
              "已经成功创建了"+num+"文件夹...")
    else:
        print(num + "文件夹已经存在...")
    MDPath = LeetCode_Path+num+"/"+num+".md"
    if not os.path.exists(MDPath):
        MDfile = open(MDPath, 'w', encoding='utf8')
        text = Make_MD_Text(num)
        text = str(text, encoding="utf-8")
        MDfile.write(text)
        MDfile.close()
        print(num+".md创建成功")
    else:
        c = input(num+".md已经存在,是否删除？(Y/N)")
        if c == "Y" or c == "y":
            os.remove(MDPath)
            c = input("是否重新创建(Y?N)")
            if c == "Y"or c == "y":
                MDfile = open(MDPath, 'w', encoding='utf8')
                text = Make_MD_Text(num)
                text = str(text, "utf-8")
                MDfile.write(text)
                MDfile.close()
                print(num+".md创建成功")
        else:
            print(num+"没有被删除")


# 修改README.md
def Update_RDM(num):
    pass


# 主函数
def main():
    os.system("cls")
    print("start!")
    for i in range(1, 601):
        Make_MD_File(i, text)


main()
