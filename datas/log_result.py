# -*-Coding =utf-8 -*-

# @Time :2024/3/30 2:36

# @Author :jiajia

# @File:log_result.py

# @software：PyCharm

# 读取日志文件，进行解析，找出日志中以[INFO]:>>当前执行脚本 开头以<<结尾的内容，将其转换为字典，然后将字典内容筛选后发送钉钉通知
import re
import json
import requests

secret = 'SECcbc9a1341b1e1116e15a4fdae35a2363dbe247b4685b8307cc073d3a7a66dc5e'
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=b587ce9ea14a5ddc58cb687896655f32e789651ecda8d0276229f372788cb9b8'
msgtype = 'markdown'

def read_log():
    with open("./logs/info.log", "r", encoding="utf-8") as f:
        data = f.read()
        cases_result_list = []
        pattern = r"\[INFO\]:>>当前执行脚本：(.*?)，用例名称：(.*?)，执行结果：(.*?)，失败原因：(.*?)<<"
        results = re.findall(pattern, data, re.S)
        for i in results:
            head = ("当前执行脚本", "用例名称", "执行结果", "失败原因")
            result = dict(zip(head, i))
            cases_result_list.append(result)
    return cases_result_list

def case_result():
    """
    获取测试用例执行结果，并发送告警通知。

    Returns:
        None
    """
    from datas.ddtalk import send_alert
    from datas.gptdemo import Gptdemo
    cases_result_list = read_log()
    total_case = len(cases_result_list)
    success_case = 0
    failed_case = 0
    success_case_name = ""
    failed_case_name = ""
    failed_reason = ""
    for result in cases_result_list:
        if result["执行结果"] == "passed":
            success_case += 1
            success_case_name += result["用例名称"] + ","
        else:
            failed_case += 1
            failed_case_name += result["用例名称"] + ","
            failed_reason += result["失败原因"] + ","
    success_case_name = success_case_name[:-1]
    failed_case_name = failed_case_name[:-1]
    failed_reason = failed_reason[:-1]
    table_total = f"| 测试用例总数 | 执行成功数 | 执行失败数 | \n" \
                  f"| --- | --- | --- | \n" \
                  f"| {total_case} | {success_case} | {failed_case} | \n"
    table_success = f"| 执行成功用例名称 | \n" \
                    f"| --- | \n" \
                    f"| {success_case_name} | \n"
    table_failed = f"| 执行失败用例名称 | \n" \
                   f"| --- | \n" \
                   f"| {failed_case_name} | \n"
    if failed_case > 0:
        prompt = f"你是一位测试专家，你的测试用例有些执行失败了，帮我将失败原因进行总结，失败的case的原因如下：{failed_reason}\n。你输出总结内容格式为：测试用例：取neme中的值，如163邮箱22：失败原因：失败的原因是断言失败...."
        result = Gptdemo(prompt)
        content = f"测试用例执行结果如下：\n{table_total}\n{table_success}\n{table_failed}\n 失败原因总结如下：\n\n{result}"
        send_alert(secret, webhook, msgtype, content)
    else:
        content = f"测试用例执行成功，本次执行结果如下：\n{table_total}"
        send_alert(secret, webhook, msgtype, content)

if __name__ == '__main__':
    case_result()