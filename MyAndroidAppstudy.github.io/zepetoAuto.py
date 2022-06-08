
#----------------
import pyautogui
import time

import json
#----------------

with open(r'zepetoText.txt','r') as info:
    text = info.readlines()


with open(r'locate.json','r')as f:
    json_data = json.load(f)

zepetoLocate = json_data['Zepeto']['fileName']
dirLoacte  = json_data['Zepeto']['dirLocate']

dirPath = r'C:/Users/Changgeun/Documents/pwa/MyAndroidAppstudy.github.io/MyAndroidAppstudy.github.io/image'

def uploadZepetoAutogui():
    time.sleep(1)
    pyautogui.moveTo(dirLoacte)
    print(pyautogui.position())
    time.sleep(1)
    pyautogui.click()
    pyautogui.typewrite(dirPath,interval=0.05)
    pyautogui.hotkey('ENTER')
    time.sleep(1)
    pyautogui.moveTo(zepetoLocate)
    print(pyautogui.position())

    pyautogui.click()
    pyautogui.typewrite(text[2],interval=0.05)
    #pyautogui.hotkey('ENTER')
    time.sleep(1)

    info.close()
    f.close()