
#----------------------
import pyautogui
import time
import json
import klaytninfo as info
#----------------------

with open(r'locate.json','r')as f:
    json_data = json.load(f)

dirLocate = json_data['Klaytn']['dirLocate']
fileName = json_data['Klaytn']['fileNameClickLocate']

def path():
    time.sleep(1)
    pyautogui.moveTo(dirLocate)
    pyautogui.click()
    pyautogui.typewrite(info.scriptPath,interval=0.03)
    pyautogui.hotkey('ENTER')

    pyautogui.moveTo(fileName)
    pyautogui.click()
    pyautogui.typewrite(info.scriptName,interval=0.03)
    pyautogui.hotkey('ENTER')

def keyStore():
    time.sleep(1)
    pyautogui.moveTo(dirLocate)
    pyautogui.click()
    pyautogui.typewrite(info.keyStorePath,interval=0.03)
    pyautogui.hotkey('ENTER')

    pyautogui.moveTo(fileName)
    pyautogui.click()
    pyautogui.typewrite(info.keyStoreName,interval=0.03)
    pyautogui.hotkey('ENTER')

time.sleep(1)
print(pyautogui.position())