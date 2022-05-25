from typing import OrderedDict
import torch
import cv2
# 출처: https://github.com/niconielsen32/ComputerVision/blob/master/yoloCustomObjectDetection.py
class Detection:
    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.detectInfoList=[]
        print("Using Device: ", self.device)
    def load_model(self, model_name):
        if model_name:
            try:
                model = torch.hub.load('./yolov5-master', 'custom', path=model_name, force_reload=True,source="local")
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

    def class_to_label(self, x):
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        self.detectInfoList=[]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.3:
                x1, y1, x2, y2 = int(
                    row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                #print("predict: ",row[4])
                #print(x1,y1,x2,y2)
                #print(x_shape,y_shape)
                #print(self.class_to_label(labels[i]))
                info={
                    "Accuracy":row[4],
                    "Label":self.class_to_label(
                    labels[i]),
                    "Box":OrderedDict({
                    "x1":x1,"x2":x2,"y1":y1,"y2":y2
                }),
                    "Size":OrderedDict({
                        "width":x_shape,
                        "height":y_shape
                    }),
                }
                self.detectInfoList.append(info)
        return frame

    def __call__(self):
        frame=cv2.imread("./test.jpg")
        frame = cv2.resize(frame, (416, 416))

        results = self.score_frame(frame)
        frame = self.plot_boxes(results, frame)

        cv2.imshow('YOLOv5 Detection', frame)
        print(self.detectInfoList)
        cv2.waitKey()
        if cv2.waitKey(5) & 0xFF == 27: 
            cv2.destroyAllWindows()

# Create a new object and execute.
detector = Detection(capture_index=0, model_name='./bestNail.pt')
detector()
