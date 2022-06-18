import pyautogui as gui
import time
size=gui.size()
print(gui.size())
#size:1920 x 1080
time.sleep(2)
print(gui.position())
# file loc: 97 x 37
gui.moveTo(97,37)
gui.click()
gui.moveTo(141,100)
gui.click()
# openProject loc: 141 x 100


nowLoc=lambda x,y:(x[0]*y[0]/100,x[1]*y[1]/100)
locate={
    "File":fnLoc((97,37)),
    "Open Project":fnLoc((141,100)),
}
print(locate)
print(nowLoc(size,locate["File"]))