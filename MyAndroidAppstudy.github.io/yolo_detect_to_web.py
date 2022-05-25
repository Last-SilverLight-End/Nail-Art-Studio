#욜로에서 추출한 이미지의 bounding box 정보 Json 객체로 전송
# Json 구조: {
#   Accuracy: 0...1,
#   Label:string
#   box:{
#   x1,x2,x3,x4
# } => 0 to 1 값
#   imgSize:[width,height]
# }
from typing import OrderedDict
from sqlalchemy import false
import torch
import cv2
import os
# 출처: https://github.com/niconielsen32/ComputerVision/blob/master/yoloCustomObjectDetection.py


def createFolder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir
    except OSError:
        print("Error: Creating dir:"+dir)

class Detection:
    def __init__(self, image, model_name):
        self.rawImage = image
        self.image=None
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.detectInfo={}
        self.isDetected=False
        print("Using Device: ", self.device)
        self.__call__()

    def load_model(self, model_name):
        if model_name:
            try:
                model = torch.hub.load(r"./yolov5-master",
                                    'custom', path=model_name, force_reload=True, source="local")
                return model
            except:
                print("Model Name is Wrong!!")
                return None

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):return self.classes[int(x)]

    def plot_boxes(self, results, rawImage):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = rawImage.shape[1], rawImage.shape[0]
        for i in range(n):
            row = [round(float(v), 4)for v in cord[i]]
            if row[4] >= 0.3:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                label=self.class_to_label(labels[i])
                tempDict={
                        "Accuracy": row[4],
                        "Box": OrderedDict({"x1": x1, "x2": x2, "y1": y1, "y2": y2}),
                    }
                self.detectInfo[label] =tempDict if label not in self.detectInfo else (
                    tempDict if self.detectInfo[label]["Accuracy"]<row[4] else self.detectInfo[label])
        self.isDetected,self.detectInfo=[True,self.detectInfo] if set(self.detectInfo.keys())==set(self.classes) else [False,{}]
        self.save_as_json()

    def save_as_json(self,path=os.path.abspath(".")+"/DetectStructure.json"):
        import json
        with open(createFolder(path),"w") as f:
            f.write(json.dumps(self.detectInfo))

    def draw_box(self,rawImage):
        if self.isDetected:
            for (key,value) in self.detectInfo.items():
                [x1,x2,y1,y2]=[i for i in value["Box"].values()]
                cv2.rectangle(rawImage, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(rawImage, key, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
        else:
            cv2.putText(rawImage,"Is Undetected!!",(0,100),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        self.image=rawImage

    def __call__(self):
        image=cv2.resize(cv2.imread(self.rawImage) if (type(self.rawImage) is str) else self.rawImage, (416, 416))
        results = self.score_frame(image)
        self.plot_boxes(results, image)
        self.draw_box(image)

    def getImage(self):
        if self.image is None:
            print("Call this instance")
            return self.rawImage
        return self.image
    def getDetectInfo(self):

        return self.detectInfo

# Create a new object and execute.
'''
detector = Detection(image="./hello.jpg", model_name='nail_best.pt')
detector()
print(detector.getDetectInfo())
'''
