from logging import exception
from pywinauto import application
import time
def processcontain(name):
    procs=application.findwindows.find_elements()
    for proc in procs:
        if proc.name==name:
            return True
    return False

def processget(name):
    procs=application.findwindows.find_elements()
    try:
        for proc in procs:
            if proc.name==name:
                return proc
        Exception(f"There is no process: {name}")
    except Exception as e:
        print(e)
        return None

def CheckUpInvoke(dlg):
    try: dlg.window_text()
    except: return False
    else: return True

def close_window(app, name):
    dlg = app[name]["TitleBar"]
    dlg.child_window(title="닫기", control_type="Button").click()

def isrun():
    procs = application.findwindows.find_elements(title_re=".*Lens Studio")
    if len(procs) != 0:
        for proc in procs:
            app = application.Application(
                backend="uia").connect(process=proc.process_id)
            dlg = app['Lens Studio']["Static"]
            if CheckUpInvoke(dlg):
                close_window(app, "Lens Studio")
    procs = application.findwindows.find_elements(
        title_re=".*Project Backup Recovery")
    if len(procs) != 0:
        app = application.Application(
            backend="uia").connect(process=proc.process_id)
        close_window(app, "Project Backup Recovery")

def findAndRemove(title):
    procs = application.findwindows.find_elements(title_re=f".*{title}")
    try:
        if not procs: raise Exception(f"없는 element, title:{title}")
        for proc in procs:
            app = application.Application(
                backend="uia").connect(process=proc.process_id)
            dlg = app[title]["Static"]
            if CheckUpInvoke(dlg): close_window(app, title)
    except Exception as e:
        print(e)