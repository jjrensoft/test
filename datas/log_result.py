# -*-Coding =utf-8 -*-

# @Time :2024/3/30 2:36

# @Author :jiajia

# @File:log_result.py

# @software：PyCharm

#读取日志文件，进行解析，找出日志中以[INFO]:>>当前执行脚本 开头以<<结尾的内容，将其转换为字典，然后将字典内容筛选后发送钉钉通知
import re
import json
import requests

def read_log():
    with open("./logs/info.log","r",encoding="utf-8") as f:
        data = f.read()
        #case_list = re.findall(r"\[INFO\]:>>(.*?)<<",data,re.S)
        #print(case_list)
        for i in re.findall(r"\[INFO\]:>>(.*?)<<",data,re.S):

            #将当前文本“当前执行脚本：cases/test_main.py::test_main_page，用例名称：163邮箱，执行结果：passed，失败原因：None” 转换为字典
            #{"当前执行脚本":"cases/test_main.py::test_main_page","用例名称":"163邮箱","执行结果":"passed","失败原因":"None"}
            i = i.replace("，",",")
            i = i.replace("：",":")
            i = i.split(",")
            result = {}
            for j in i:
                j = j.split(":")
                result[j[0]] = j[1]
            #print(result)
            print(f'用例名称：{result["用例名称"]},执行结果：{result["执行结果"]}')

if __name__ == '__main__':
    read_log()