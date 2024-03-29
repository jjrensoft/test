# -*-Coding =utf-8 -*-

# @Time :2024/3/29 0:33

# @Author :jiajia

# @File:data_load.py

# @software：PyCharm
import yaml
import os

def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

get_data = load_yaml("./datas/data.yaml")
print(get_data)
if __name__ == '__main__':
    #获取当前执行路径
    current_path = os.path.dirname(__file__)
    print(current_path)
    #拼接yaml文件路径
    file ="./datas/data.yaml"
    data = load_yaml(file)
    print(data)
    print(data["sucessful_login"]["user"])
    print(type(data["sucessful_login"]))
    print(type(data["error_login"]))

