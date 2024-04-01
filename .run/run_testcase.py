# -*-Coding =utf-8 -*-

# @Time :2024/3/30 21:24

# @Author :jiajia

# @File:run_testcase.py

# @software：PyCharm
import pytest
import os
from datas.log_result import case_result

# 执行测试用例
if __name__ == '__main__':
    # 如果logs/info.log文件存在，删除
    if os.path.exists("logs/info.log"):
        os.remove("logs/info.log")

    # 获取当前执行路径
    current_path = os.path.dirname(__file__)

    # 指定执行目录中的测试用例
    # test_directory = os.path.join(current_path, "./pages")  # 替换为你的测试目录路径
    # test_directory = ("./pages")  # 替换为你的测试目录路径

    # 执行测试用例
    # pytest.main(["-s", "-v", "--alluredir", "./report/allure-results", test_directory])
    pytest.main(["-s", "-v", "--alluredir", "./report/allure-results"])

    # 生成测试结果报告
    case_result()
