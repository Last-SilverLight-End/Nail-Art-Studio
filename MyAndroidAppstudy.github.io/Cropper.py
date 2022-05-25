from cv2 import hconcat
from yolo_detect_to_web import Detection
from typing import OrderedDict
from charset_normalizer import detect
import cv2
import os
from glob import glob
import numpy as np
def createFolder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir
    except OSError:
        print("Error: Creating dir:"+dir)

class Cropper:
    def __init__(self,image_path,data):
        self.rawImage=os.path.abspath(".")+"/"+image_path
        self.rawFileName=image_path.split(".")[0]
        self.Data=data
        self.Image=None
        self.openCV_dict={}
        self.__call__()
    def __call__(self):
        self.Image=cv2.imread(self.rawImage)
        swapper=lambda a,b:[a,b] if a<b else [b,a]
        for key,val in self.Data.items():
            [x1,x2,y1,y2]=[val["Box"][v] for v in ["x1","x2","y1","y2"]]
            [x1,x2],[y1,y2]=swapper(x1,x2),swapper(y1,y2)
            output=self.Image[y1:y2,x1:x2].copy()#얕은 복사!! .copy()=> 깊은 복사!!
            self.openCV_dict[key]=output
    
    def img_save(self,dir_path):#현재 저장하는 디렉토리 최종 위치만 저장
        dir=createFolder(os.path.abspath(".")+f"/{dir_path}/")
        for key,val in self.openCV_dict.items():
            cv2.imwrite(dir+f"{key}_{self.rawFileName}.jpg",val)
    def get_opencv_dict(self):
        return self.openCV_dict
    def save_as_json(self,dir_path):
        import json
        with open(dir_path,"w+") as f:
            f.write(json.dumps({key: val.tolist() for key,val in self.openCV_dict.items()}))
def openJsonPath(fileName):
    import json
    with open(os.path.abspath(".")+"/"+fileName,"r") as f:
        data=json.load(f)
    return data
cropper=Cropper("05_06_True_24.jpg",openJsonPath("DetectStructure.json"))
#cropper.img_save("FingerData")
dict=cropper.get_opencv_dict()
cropper.save_as_json(os.path.abspath(".")+"/FingerJsonData.json")
def MergeNails(dict):
    start=None
    for key in ["Thumb","Index","Middle","Pinky","Ring"]:
        temp=cv2.resize(dict[key],(100,100))
        start=temp if start is None else cv2.hconcat((start,temp))
    cv2.imshow("start",start)
    cv2.waitKey()
MergeNails(dict)