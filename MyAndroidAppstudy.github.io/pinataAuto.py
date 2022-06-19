
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
imagelastbtn = json_data['Pinata']['imagelastbtn']

# 여기에서 디렉토리 수정하기
dirPath = r'C:/Users/xnote/OneDrive/문서/reactCreateProject/MyAndroidAppstudy.github.io/MyAndroidAppstudy.github.io'
def uploadImageAuto():
    
    time.sleep(2)
    pyautogui.moveTo(Imageupload)
    time.sleep(3)
    pyautogui.click()
    time.sleep(2)

    pyautogui.moveTo(dirLoacte)
    print(pyautogui.position())
    time.sleep(3)
    pyautogui.click()
    pyautogui.typewrite(dirPath,interval=0.03)
    pyautogui.hotkey('ENTER')

    pyautogui.moveTo(fileNameClickLocate)
    pyautogui.click()
    pyautogui.typewrite(text.file_name,interval=0.03)
    pyautogui.hotkey('ENTER')
    time.sleep(3)
    pyautogui.moveTo(imagelastbtn)
    pyautogui.click()


def uploadPinataAutogui():
    time.sleep(3)
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


# time.sleep(3)
# print(pyautogui.position())
