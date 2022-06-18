from pywinauto import Application
from urllib import request
import os
import asyncio
from selenium import webdriver
import time
from Process import Process

class WindowEvent:
    @staticmethod
    def close(App):
        dlg = App["TitleBar"]
        dlg.child_window(title="닫기", control_type="Button").click()
    @staticmethod
    def maximize(App,Title):
        dlg=App[Title]["TitleBar"]
        dlg.print_control_identifiers()
        dlg.child_window(title="최대화", control_type="Button").click()
def getURL():
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    dlg = app.top_window()
    url = dlg.child_window(title="주소창 및 검색창", control_type="Edit").get_value()
    dlg.type_keys("%{F4}") # Alt-F4
    return url
def SubmitPage(url):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('./getURL/chromedriver.exe', options=options)
    driver.implicitly_wait(100)
    driver.get(url)
    time.Delay(5)
    return True
#SubmitPage("a")
'''
1. 셀레니움 사용 => 페이지 완료
2. 계속 통신
'''
def getURL2(Browser="Chrome"):
    proc=Process.getProcess(Browser)
    app=Process.getApp(proc)
    dlg=app.top_window()
    print(dlg.child_window(title="주소창 및 검색창", control_type="Edit"))
    url = dlg.child_window(title="주소창 및 검색창", control_type="Edit").get_value()
    return url

print(getURL2())