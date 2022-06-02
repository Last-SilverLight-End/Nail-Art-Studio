from charset_normalizer import detect
import numpy as np
from ZepetoMain import AutoProcess
from flask_cors import CORS
from PIL import Image
from yolo_detect_to_web import Detection
import base64
import cv2
from asyncore import write
import os
import io
import sys
import py_compile
from tkinter import W
from flask import Flask, render_template, request, session, Blueprint, jsonify
from werkzeug.utils import secure_filename
import logging
import imghdr
from Cropper import Cropper ,Merge
logger = logging.getLogger('HELLO WORLD')
from typing import OrderedDict

app = Flask(__name__)
CORS(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# 여기에서 upload 파일 루트 변경해 줘야 한다.
UPLOAD_FOLD = './image'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLD

# 서버 킬때 기본으로 나오는 부분


@app.route('/')
def hello():
    return 'hello!'
# test communicate


@app.route('/api')
def hellos():
    return{
        'hola': "oh yeah"
    }
# change image file how much big or not


def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

# send upload but must to fix it


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    f = request.files['file']
    f.save(os.path.join(
        app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return 'file uploaded successfully'

# 여기에서 서버에서 ZepetoInfo 변경 해야 한다 나중에 알략님께 물어볼것


@app.route('/changeZepetoInfo', methods=["POST", "GET"])
def change_file_Zepeto():
    id_request = request.form.get('data')  # cg45624364235
    pwd_request = request.form.get('pwd')  # aSDfasdfasfda
    text_file_path = 'zepetoText.txt'
    new_text_content = ''
    print(id_request)
    print(pwd_request)
    with open(text_file_path, 'r') as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            if i == 0:
                new_string = id_request
            elif i == 1:
                new_string = pwd_request
            elif i == 2:
                new_string = 'sam.png'

            if new_string:
                new_text_content += new_string + '\n'
            else:
                continue
    with open(text_file_path, 'w') as f:
        f.write(new_text_content)
        return 'file finished successfully'


# api testing data


@app.route('/data')
def User_data():
    return {
        'Name': "hello",
        'Age': "22",
        "Date": "x",
        "Cost": "1000",
    }

# 랜더링 과정 유무


@app.route('/rendering')
def Rendering():
    autoprocess = AutoProcess()
    try:
        autoprocess.main()
        return "all ok"
    except:
        return "error occured"


image=None

# 여기부터 YOLO 돌리기 위한 작업들 시작

############################################## THE REAL DEAL ###############################################
@app.route('/cropping', methods=['GET', 'POST'])
def crop_image():
    def __init__(self,opencv_dict):
        self.dict=opencv_dict
        self.nft_template=["Thumb","Index","Middle","Pinky","Ring"]
        self.zepeto_template={
        "Top":{
        "Pinky":[1,1,36,77],
        "Ring":[38,1,84,104],
        "Middle":[86,1,135,108],
        "Index":[137,1,184,106],
        "Thumb":[186,1,254,124]
        },
        "Bottom":{
        "Thumb": [2,254,69,131],
        "Index":  [71,254,118,149],
        "Middle":[120,254,169,148],
        "Pinky": [171,254,217,151],
        "Ring": [ 219,254,254,177]
        }
    }
    
    def swapper(self,a,b):
        return [a,b] if a<b else [b,a]

    def get_nft_merge(self):
        mergeImg=None
        for key in ["Thumb","Index","Middle","Pinky","Ring"]:
            print("asdfasdf : ", key)
            print(dict[key])
            #im = im.permute(0, 2, 3, 1).cpu().numpy()
            #im = Image.fromarray((im[0] * 255).astype('uint8'))
            #im = im.resize((192, 320), Image.ANTIALIAS)
            temp=cv2.resize(dict[key],(100,100),interpolation = cv2.INTER_AREA)
            mergeImg=temp if mergeImg is None else cv2.hconcat((mergeImg,temp))
        return mergeImg
        
    def get_zepeto_merge(self):
        mergeImg=255-np.zeros((256,256,3),dtype=np.uint8)
        flag=False
        for val in self.zepeto_template.values():
            flag=True
            for (key,val) in val.items():
                x1,y1,x2,y2=val
                [x1,x2],[y1,y2]=self.swapper(x1,x2),self.swapper(y1,y2)
                #print("that is : ",dict[key])
                temp=cv2.resize(dict[key],(x2-x1,y2-y1))
                mergeImg[y1:y2,x1:x2]= cv2.flip(temp,0)if flag else temp
    try:
        route_request = request.form.get('route')
        file = request.files['file'].read()
        
       # print("file is : ",file)
        print("route is :",  route_request)
        print(type(route_request))
        print(route_request)

        image=Cropper.get_img_by_path("05_06_True_24.jpg")
        #print(image)
        detect_json=Cropper.openJsonPath("DetectStructure.json")

        cropper = Cropper(image,detect_json)
        dict=cropper.get_opencv_dict()
        #print(dict)
     
        dict = np.array(dict)
        merge=Merge(opencv_dict=dict)
        print("heelo", merge.dict)
        #nft_merge_img=get_nft_merge(merge)
        zepeto_merge_img=merge.get_zepeto_merge()
        #Merge.save_img_by_path(nft_merge_img,"./image/nft_image.png")
        Merge.save_img_by_path(zepeto_merge_img,"./image/zepeto_image.png")
        print("finished")
        return "finish"
    except Exception as e:
        print("Model Name is Wrong!3!", e)
        return "error occured"


@app.route('/detectObject', methods=['GET', 'POST'])
def mask_image():
    # 1번째 작업 할일 하루 정도  + zepeto id,pwd 받아오는거
    # 2번째 cropper 적용 시키는거 하고 파일쪽으로 업로드 시키기
    # zepeto 사진 루트 정하기
    # 3일 정도 소요 예상
    # nft,snapchat 내일 준다고 가정 -> 2일 5-6일
    # css 부분 최소한 꾸미기 1일

    # print(request.files , file=sys.stderr)
    file = request.files['file'].read()  # byte file
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    image=img
    ######### Do preprocessing here ################
    # img[img > 150] = 0
    # any random stuff do here
    ################################################

    # 여기서 못받음 -> 이제 받음
    detector = Detection(img, "./nail_best.pt")
      # 여기에서 빈 객체인지 아닌지 확인  { }
    print(detector.getDetectInfo())
    tempo = "{}".format(detector.getDetectInfo())
    tempo2= "sat"
    print(tempo)
    print(type(detector.getDetectInfo()))


    if (tempo == "{}"):
        print("error")
        return "error occured"


    else:
        print("this is ok!")
        img = detector.getImage()
        img = Image.fromarray(img.astype("uint8"))
        rawBytes = io.BytesIO()
        img.save(rawBytes, "JPEG")
        rawBytes.seek(0)
        img_base64 = base64.b64encode(rawBytes.read())
        return jsonify({'status': str(img_base64)})

##################################################### THE REAL DEAL HAPPENS ABOVE ######################################


@app.route('/test', methods=['GET', 'POST'])
def test():
    print("log: got at test", file=sys.stderr)
    return jsonify({'status': 'succces'})


@app.after_request
def after_request(response):
    print("log: setting cors", file=sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(debug=True)
