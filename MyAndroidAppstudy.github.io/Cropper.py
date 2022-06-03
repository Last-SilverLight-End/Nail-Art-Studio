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
    @staticmethod
    def get_img_by_path(image_path):
        rawImage=os.path.abspath(".")+"/"+image_path
        return cv2.imread(rawImage)
    def __init__(self,image,data):
        self.rawImage=image
        self.Data=data
        self.Image=image
        self.openCV_dict={}
        self.__call__()
    def swapper(self,a,b):
        return [a,b] if a<b else [b,a]
    def __call__(self):#이미지를 자르고 merge에서 사용하는 형식으로 변환한다.
        for key,val in self.Data.items():
            [x1,x2,y1,y2]=[val["Box"][v] for v in ["x1","x2","y1","y2"]]
            [x1,x2],[y1,y2]=self.swapper(x1,x2),self.swapper(y1,y2)
            output=self.Image[y1:y2,x1:x2].copy()#얕은 복사!! .copy()=> 깊은 복사!!
            self.openCV_dict[key]=output
    def img_save(self,dir_path):#현재 저장하는 디렉토리 최종 위치만 저장
        dir=createFolder(os.path.abspath(".")+f"/{dir_path}/")
        for key,val in self.openCV_dict.items():
            cv2.imwrite(dir+f"{key}_{self.rawFileName}.jpg",val)
    def get_opencv_dict(self):
        return self.openCV_dict
    def save_as_json_opencv_dict(self,dir_path):
        import json
        with open(dir_path,"w+") as f:
            f.write(json.dumps({key: val.tolist() for key,val in self.openCV_dict.items()}))
    def openJsonPath(fileName):
        import json
        with open(os.path.abspath(".")+"/"+fileName,"r") as f:
            data=json.load(f)
        return data
def openJsonPath(fileName):
    import json
    with open(os.path.abspath(".")+"/"+fileName,"r") as f:
        data=json.load(f)
    return data

class Merge:
    @staticmethod
    def save_img_by_path(img,save_path):
        cv2.imwrite(save_path,img)
    def __init__(self,opencv_dict):
        self.dict=opencv_dict
        self.nft_template=["Thumb","Index","Middle","Pinky","Ring"]
        self.zepeto_template={
        "Top":{
        "Pinky":[1,1,36,77],
        "Ring":[38,1,84,104],
        "Middle":[86,1,135,108],
        "Index":[137,1,184,106],
        "Thumb":[186,1,254,124],
        },
        "Bottom":{
        "Thumb": [2,254,69,131],
        "Index":  [71,254,118,149],
        "Middle":[120,254,169,148],
        "Pinky": [171,254,217,151],
        "Ring": [ 219,254,254,177],
        }
    }
    def swapper(self,a,b):
        return [a,b] if a<b else [b,a]
    #제페토 형식으로 합병 후 해당 이미지 형식 반환
    def get_zepeto_merge(self):
        mergeImg=255-np.zeros((256,256,3),dtype=np.uint8)
        flag=False
        for val in self.zepeto_template.values():
            flag=True
            for (key,val) in val.items():
                x1,y1,x2,y2=val
                [x1,x2],[y1,y2]=self.swapper(x1,x2),self.swapper(y1,y2)
                temp=cv2.resize(self.dict[key],(x2-x1,y2-y1))
                mergeImg[y1:y2,x1:x2]= cv2.flip(temp,0)if flag else temp
        return mergeImg
    def get_nft_merge(self):
        mergeImg=None
        for key in self.nft_template:
            temp=cv2.resize(self.dict[key],(100,100))
            mergeImg=temp if mergeImg is None else cv2.hconcat((mergeImg,temp))
        return mergeImg
### 사용 예시
#이미지와 영역 감지 json을 경로에서 받아오는 것, 필수 아님
#image=Cropper.get_img_by_path("05_06_True_24.jpg")
#detect_json=openJsonPath("DetectStructure.json")

#이미지와 영역감지 딕셔너리으로 인스턴스 생성
#cropper=Cropper(image,detect_json)
#dict=cropper.get_opencv_dict()# {손톱 라벨: 손톱 이미지}로 매핑된 딕셔너리 구조를 반환한다.


#merge=Merge(opencv_dict=dict)#{손톱 라벨: 손톱 이미지} 딕셔너리로 인스턴스 생성
#nft_merge_img=merge.get_nft_merge()#nft 합병 이미지 가져옴
#zepeto_merge_img=merge.get_zepeto_merge()# 제페토 합병 이미지 가져옴
#Merge.save_img_by_path(nft_merge_img,"./hello.png")# 특정 디렉토리에 이미지 저장
#Merge.save_img_by_path(zepeto_merge_img,"./hello.png")# 특정 디렉토리에 이미지 저장