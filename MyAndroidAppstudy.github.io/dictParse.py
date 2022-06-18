from collections import deque
import pyautogui as gui
import json
import os
def getDict(jsonString,fn):
    def __dictRe(items,acc={}):
        if not items:
            if acc["parent"] is None: return acc["data"]
            else:
                parent=acc["parent"]
                parentKey=acc["parent"]["key"]
                parentAcc=acc["parent"]["acc"]
                parentAcc["data"][parentKey]=acc["data"]
                return _dictRe(parent["items"],parentAcc)
        else:
            (k,v)=items.popleft()
            if type(v) is dict:
                return _dictRe(v,{
                    "data":{},
                    "parent":{"key":k,"acc":acc,"items":items}
                })
            else:
                acc["data"][k]=fn(v)
                return _dictRe(items,acc)
    _dictRe=lambda data,acc:__dictRe(deque(data.items()) if type(data) is not deque else data,acc)
    DictRe=lambda data:_dictRe(data,{"data":{},"parent":None})
    return DictRe(jsonString)
def Get_GUI_Dict(fileLocation="locate.json"):
    getRealWindowSize=lambda point: tuple(map(lambda s,p: int(s*p/100),gui.size(),point))
    file=open(f"{os.path.dirname(os.path.realpath(__file__))}\{fileLocation}")
    jsonString=json.load(file)
    return getDict(jsonString,getRealWindowSize)
