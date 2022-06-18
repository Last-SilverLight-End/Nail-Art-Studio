
import pyautogui as gui
import json
from collections import OrderedDict

def choose():
    for v in gui.getWindowsWithTitle("Choose project file"):
        v.activate()
        v.maximize()

def getReal(point):
    size=gui.size()
    x=size[0]*point[0]/100
    y=size[1]*point[1]/100
    return (int(x),int(y))
'''    
if type(data) is dict:
        if keys is not False:
            newData=data[keys.shift()]
            if type(newData) is dict:
                newKeys=list(newData.keys())
                return _changeRealPosition(newData,newKeys,stack.append({
                    "prev_prev":stack,
                    "prev":data,
                    "keys":keys,
                }))
            else: return _changeRealPosition(newData,[],stack.append({
                    "prev_prev":stack,
                    "prev":data,
                    "keys":None,
                }))
        else:
            return _changeRealPosition()

'''

def _changeRealPosition(data):
    if type(data) is dict:
        newJson={}
        for v in list(data.keys()):
            a=_changeRealPosition(data[v]) # 스택 구조가 일어난다.
            newJson[v]=a
        return newJson
    else: return getReal(data)

def _changePosition(data,i,acc={}):
    if type(data) is dict:
        #return recurSion(data,len(data.keys())-1,{})
        if i<0:
            return acc
        else:
            li=list(data.keys())
            acc[li[i]]=_changePosition(data[li[i]],i-1,acc)
            return acc
    else:
        newData=getReal(data)

def recurSion(data,i,acc={}):
    if i<0:
        return acc
    else:
        li=list(data.keys())
        acc[li[i]]=_changePosition(data[li[i]])
        return recurSion(data,i-1,acc)

def changeRealPosition(json):
    if type(json) is dict:
        #return _changeRealPosition(list(jsonString.items()))
        return _changePosition(json,len(list(json.keys()))-1)
    else:
        print("에러")
        return False

def openProject():
    file=open("./locate.json")
    jsonString=json.load(file)
    LensStudio=OrderedDict(jsonString["Lens Studio"])
    od=OrderedDict()
    for key,value in LensStudio.items():
        od[key]=getReal(value)
    print(od["File"])


file=open(".\locate.json")
jsonString=json.load(file)
#print(type(jsonString))
#print(list(jsonString.items())[0][0])
print(changeRealPosition(jsonString))