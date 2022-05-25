import cv2
import json
import os
import numpy as np
def openJsonPath(fileName):
    import json
    with open(os.path.abspath(".")+"/"+fileName,"r") as f:
        data=json.load(f)
    return data

def MergeNails(dict):
    print(type(dict))
    start=None
    for key in ["Thumb","Index","Middle","Pinky","Ring"]:
        print(type(dict[key]))
        temp=cv2.resize(dict[key],(100,100))
        start=temp if start is None else cv2.hconcat((start,temp))
    cv2.imshow("start",start)
    cv2.waitKey()


jsonData=openJsonPath("FingerJsonData.json")
mydict={key:np.array(val,dtype=np.int32) for key,val in jsonData.items()}
MergeNails(mydict)


class Merge:
    def __init__(self):
        pass