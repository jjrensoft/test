# -*-Coding =utf-8 -*-

# @Time :2024/3/23 1:44

# @Author :jiajia

# @File:login_get_cookie.py

# @software：PyCharm

import pytest
from datas.data_load import get_data
@pytest.mark.parametrize("logindata",get_data)
def test_login(page,logindata):
    print(f"-------{get_data['sucessful_login']['user']}----------")
    page.goto("https://mail.163.com")
    # 等待加载完成
    page.wait_for_load_state("domcontentloaded")
    # 切换到iframe
    iframe = page.query_selector("#loginDiv iframe")
    iframe_page = iframe.content_frame()
    # 输入用户名和密码
    iframe_page.fill("input[name='email']",f"{get_data['sucessful_login']['user']}")
    iframe_page.fill("input[name='password']",f"{get_data['sucessful_login']['password']}")
    iframe_page.click("#dologin")
    page.wait_for_url("**/main.jsp**")
    # 储存登录cookie
    page.context.storage_state(path="auth/cookie.json")
