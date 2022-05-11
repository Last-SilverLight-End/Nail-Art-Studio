
#----------------
import pyautogui
import time
import zepetoInfo as zepeto
import json
#----------------

with open(r'locate.json','r')as f:
    json_data = json.load(f)

zepetoLocate = json_data['Zepeto']['fileName']
dirLoacte  = json_data['Zepeto']['dirLocate']

dirPath = r'C:/Users/mvr/Desktop/image'

def uploadZepetoAutogui():
    time.sleep(1)
    pyautogui.moveTo(dirLoacte)
    print(pyautogui.position())
    pyautogui.click()
    pyautogui.typewrite(dirPath,interval=0.05)
    pyautogui.hotkey('ENTER')
    time.sleep(1)
    pyautogui.moveTo(zepetoLocate)
    print(pyautogui.position())

    pyautogui.click()
    pyautogui.typewrite(zepeto.fileName,interval=0.05)
    pyautogui.hotkey('ENTER')
