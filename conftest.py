# -*-Coding =utf-8 -*-

# @Time :2024/3/23 1:11

# @Author :jiajia

# @File:confset.py

# @software：PyCharm

from playwright.sync_api import sync_playwright
import pytest
from log import logger

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        viewport = {"width": 1920, "height": 1080}
        context = browser.new_context(permissions=permissions, viewport=viewport)
        page = context.new_page()
        # Disable webdriver detection
        s = " delete Object.getPrototypeOf(navigator).webdriver "
        page.add_init_script(s)
        yield page
        page.close()
        browser.close()
@pytest.fixture(scope="session")
def web_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        viewport = {"width": 1920, "height": 1080}
        storage_state = "auth/cookie.json"
        context = browser.new_context(permissions=permissions, viewport=viewport,storage_state=storage_state)
        page = context.new_page()
        # Disable webdriver detection
        s = " delete Object.getPrototypeOf(navigator).webdriver "
        page.add_init_script(s)
        yield page
        page.close()
        browser.close()

@pytest.fixture(scope="function")
def web_page_new():
    with sync_playwright() as p:
        logger.info("page session fixture starting....")
        browser = p.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        viewport = {"width": 1920, "height": 1080}
        storage_state = "auth/cookie.json"
        context = browser.new_context(permissions=permissions, viewport=viewport, storage_state=storage_state)
        page = context.new_page()

        # Disable webdriver detection
        s = " delete Object.getPrototypeOf(navigator).webdriver "
        page.add_init_script(s)
        logger.info("start tracing...")
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page

        logger.info("page session fixture closing.......")
        context.tracing.stop(path="trace.zip")
        logger.info("stop tracing...")

        page.close()
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
#item：代表当前的测试用例项（test item），包括测试用例的名称、标记、位置等信息。item：代表当前的测试用例项（test item），包括测试用例的名称、标记、位置等信息。
def pytest_runtest_makereport(item):
    # 使用 yield 语句获取钩子方法的调用结果（out），这里是获取测试用例的测试结果
    out = yield
    #获取执行结果
    report=out.get_result()
    #打印用例执行状态，例如用例名称,执行结果，失败原因
    if report.when == "call":
        marker = item.get_closest_marker("name")
        print('执行脚本：{}，用例名称：{}，执行结果：{}，失败原因：{}'.format(report.nodeid,marker.args[0], report.outcome, report.longrepr))
        #将结果存入字典并打印字典
        dict = {}
        dict['执行脚本'] = report.nodeid
        dict['用例名称'] = marker.args[0]
        dict['执行结果'] = report.outcome
        dict['失败原因'] = report.longrepr
        logger.info('>>当前执行脚本：{}，用例名称：{}，执行结果：{}，失败原因：{}<<'.format(report.nodeid,marker.args[0], report.outcome, report.longrepr))
        print(dict)
