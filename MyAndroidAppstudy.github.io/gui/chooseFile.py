from concurrent.futures import process
from logging import exception
from pywinauto import application
import pyautogui
#Choose project file
title0="Lens Studio"
title1="Choose project file"
procs=application.findwindows.find_elements(title_re=f".*{title0}")
for proc in procs:
    app=application.Application(backend="uia").connect(process=proc.process_id)
    app=app.window(title_re=f".*{title0}")
    app=app[title1]
    app.set_focus()
    app.print_control_identifiers()
    pyautogui.keyDown('backspace')
    pyautogui.keyDown('backspace')
    #dlg=app["TitleBar"]
    print("----------------------------------------------------------")
    #dlg.child_window(title="최대화", control_type="Button").click()
    #dlg.type_keys("주소: asdf")