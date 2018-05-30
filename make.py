#coding=utf-8
# 这是一个用于爬取Leetcode网页
# 并自动创建刷题md文档的python脚本

import requests
import os

# url使用leetcode中国
Leetcode_CN_Url = "https://leetcode-cn.com/problemset/all/"
Leetcode_Url = "https://leetcode.com/problemset/all/"

# 爬取题目
def GetProblem(num,url):



# 创建md文档
def MakeMD(num):



# 修改README.md 
def Update_RDM(num):



# 主函数
def main():
    num = imput("请输入要刷的题号：")
    soup = GetProblem(num,Leetcode_CN_Url)
    MakeMD(num)
    Update_RDM(num)
    print("make complete!")


main()

