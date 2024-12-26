# -*-Coding =utf-8 -*-

# @Time :2024/3/30 23:20

# @Author :jiajia

# @File:gptdemo.py

# @software：PyCharm
# 设置 OpenAI API 访问 Token
import requests
def Gptdemo(msg: str) -> str:
    url = ""
    api_token = ""
    headers = {
        "Authorization": f"Basic {api_token}",
        "Content-Type": "application/json",
    }
    # 调用 OpenAI GPT API 生成回复
    data = {
            "frequency_penalty": 0,
            "max_tokens": 2048,
            "message": msg,
            "model": "gpt-3.5-turbo",
            "n": 1,
            "presence_penalty": 0,

            "role": "assistant",
            "seed": 0,
            "stop": [
                "string"
            ],
            "stream": False,
            "temperature": 0,
            "top_p": 1,
            "user": ""
    }
    response = requests.post(
        f"{url}/compute/openai_chatgpt_turbo", json=data, headers=headers
    )
    # 解析 OpenAI GPT API 的响应并输出回复
    response_data = response.json()["data"]["message"]
    return response_data
