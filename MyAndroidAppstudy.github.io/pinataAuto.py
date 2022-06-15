
#----------------
import pyautogui
import time

from pydantic import PaymentCardNumber
import text
import json
#----------------

with open(r'locate.json','r')as f:
    json_data = json.load(f)

dirLoacte  = json_data['Pinata']['dirLocate']
#uploadBtn = json_data['Pinata']['uploadButtonForDir']
uploadBtn = json_data['Pinata']['uploadbtn']
Imageupload = json_data['Pinata']['selectaFile']
fileNameClickLocate = json_data['Pinata']['fileNameClickLocate']

dirPath = r'C:/Users/mvr/Desktop/JM/NFT/'
def uploadImageAuto():
    time.sleep(1)
    pyautogui.moveTo(Imageupload)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(dirLoacte)
    print(pyautogui.position())
    time.sleep(1)
    pyautogui.click()
    pyautogui.typewrite(dirPath,interval=0.03)
    pyautogui.hotkey('ENTER')

    pyautogui.moveTo(fileNameClickLocate)
    pyautogui.click()
    pyautogui.typewrite(text.file_name,interval=0.03)
    pyautogui.hotkey('ENTER')


def uploadPinataAutogui():
    time.sleep(1)
    pyautogui.moveTo(dirLoacte)
    print(pyautogui.position())
    pyautogui.click()
    pyautogui.typewrite(dirPath+text.username,interval=0.03)
    pyautogui.hotkey('ENTER')
    #---movedir

    pyautogui.moveTo(uploadBtn)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('LEFT')
    pyautogui.hotkey('ENTER')


time.sleep(1)
print(pyautogui.position())