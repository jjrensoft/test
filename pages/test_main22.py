# -*-Coding =utf-8 -*-

# @Time :2024/3/23 3:53

# @Author :jiajia

# @File:test_main22.py.py

# @software：PyCharm
import pytest
@pytest.mark.name("163邮箱22")
def test_main_page2(web_page_new):
    web_page_new.goto("https://mail.163.com/js6/main.jsp")
    web_page_new.wait_for_load_state("domcontentloaded")
    web_page_new.get_by_role("button", name="收 信").click()
    web_page_new.wait_for_load_state("networkidle")
    web_page_new.screenshot(path="163.png")
    assert web_page_new.title() == "网易邮箱测试"


