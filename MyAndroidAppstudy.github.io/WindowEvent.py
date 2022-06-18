import pyautogui as gui
from dictParse import Get_GUI_Dict
import time
class WindowEvent:
    @staticmethod
    def size():
        gui.size()
    @staticmethod
    def maximize():
        gui.hotkey("Alt","Space","X")
        return WindowEvent
    @staticmethod
    def click(location,timeDelay=1):
        gui.click(location)
        time.sleep(timeDelay)
        return WindowEvent
    @staticmethod
    def setText(text,interval=0.1,timeDelay=1):
        gui.typewrite(text,interval=interval)
        time.sleep(timeDelay)
        return WindowEvent
    @staticmethod
    def exit():
        gui.hotkey("Alt","F4")
        return WindowEvent
    @staticmethod
    def press(key):
        li=["enter",'c']
        if key in li: gui.press(key)
        return WindowEvent
'''
time.sleep(2)
GUI_Dict=Get_GUI_Dict()
lensGUI=GUI_Dict["Lens Studio"]
FileChoose=GUI_Dict["Choose project file"]
filePath="C:/nailTracking"
fileName="nailTracking"
WindowEvent.click(lensGUI["File"],).click(lensGUI["Open Project"]).click(FileChoose["Address_Bar"]
).setText(filePath).press("enter").click(FileChoose["FileName_Bar"]).setText(fileName
).click(FileChoose["Open"])
'''