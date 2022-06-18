from tkinter import Y
import pyautogui as gui
import time
def changeReal(point):
    size=gui.size()
    x=size[0]*point[0]/100
    y=size[1]*point[1]/100
    return (x,y)

def fnLoc(loc,absP=(1920,1080)):
    x=100*loc[0]/absP[0]
    y=100*loc[1]/absP[1]
    return (x,y)
size=gui.size()
print(gui.size())
time.sleep(3)
print(gui.position())
print(fnLoc(gui.position()))
#459,56
#projectFileText:(28.125, 5.37037037037037)
#'' FileName:(29.114583333333332, 90.27777777777777)
#'' open:(90.52083333333333, 92.5)
'''
Publish Lens: (7.916666666666667, 5.185185185185185)
'''