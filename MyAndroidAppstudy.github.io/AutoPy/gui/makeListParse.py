li=[1,2,3,[4,5,6,[7,8,9]],10]
dic={
    "data":[],
    "parent":False
}
def liRe(li,i=0,acc={}):
    if len(li)<=i:
        if acc["parent"] is False:
            return acc
        else:
            parent=acc["parent"]
            parent["acc"]["data"].append(acc["data"])
            newLI=parent["li"]
            newI=parent["i"]+1
            return liRe(newLI,newI,parent["acc"])
    else:
        data=li[i]
        if type(data) is list:
            return liRe(data,0,{
                "data":[],
                "parent":{
                    "acc":acc,
                    "li":li,
                    "i":i
                }
            })
        else:
            acc["data"].append(data)
            return liRe(li,i+1,acc)
dic={
    "a":1,
    "b":{
        "c":2,
        "d":4,
        "e":{"f":3}
    }
}
import pyautogui as gui
getRealWindowSize=lambda point: tuple(map(lambda s,p: s*p/100),gui.size(),point)
def dictRe(dic,i=0,acc={}):
    items=list(dic.items())
    if len(items)<=i:
        if acc["parent"] is None:
            return acc["data"]
        else:
            parent=acc["parent"]
            parentKey=acc["parent"]["key"]
            parentAcc=acc["parent"]["acc"]
            parentAcc["data"][parentKey]=acc["data"]
            return dictRe(parent["dic"],parent["i"]+1,parentAcc)
    else:
        (k,v)=items[i]
        if type(v) is dict:
            return dictRe(v,0,{
                "data":{},
                "parent":{"key":k,"acc":acc,"dic":dic,"i":i}
            })
        else:
            acc["data"][k]=v
            return dictRe(dic,i+1,acc)

print(dictRe(dic,0,{"data":{},"parent":None}))
#print(liRe(li,0,dic))