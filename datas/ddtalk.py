# -*-Coding =utf-8 -*-

# @Time :2024/3/30 22:37

# @Author :jiajia

# @File:ddtalk.py

# @software：PyCharm
import base64
import urllib
import requests
import logging
import time
import hmac
import hashlib

def send_alert(secret: str, webhook: str, msgtype: str, content: str) -> None:
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    webhook = f'{webhook}&timestamp={timestamp}&sign={sign}'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": msgtype,
        "markdown": {
            "title": "UI自动化通知",  # 添加title键和对应的值
            "text": content
        }
    }
    response = requests.post(webhook, headers=headers, json=data)
    if not response.ok:
        logging.error(f"Failed to send alert: {response.text}")