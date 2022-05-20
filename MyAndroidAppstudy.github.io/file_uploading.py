from asyncore import write
import os
import py_compile
from tkinter import W
from flask import Flask, render_template, request, session ,Blueprint
from werkzeug.utils import secure_filename
import logging
import imghdr
logger = logging.getLogger('HELLO WORLD')
import zepetoInfo
from ZepetoMain import AutoProcess


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#여기에서 upload 파일 루트 변경해 줘야 한다.
UPLOAD_FOLD = './public'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 서버 킬때 기본으로 나오는 부분
@app.route('/')
def hello():
    return 'hello!'
# test communicate
@app.route('/api')
def hellos():
    return{
        'hola' : "oh yeah"
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
@app.route('/uploader', methods = ['GET','POST'])
def uploader_file():
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

    
    return 'file uploaded successfully'
#여기에서 서버에서 ZepetoInfo 변경 해야 한다 나중에 알략님께 물어볼것
@app.route('/changeZepeto_Info', methods = ["POST"])
def change_file_Zepeto():
    edited_lines = []
    with open(zepetoInfo) as f:
        lines = f.readlines()
        for line in lines:
            if 'id' in line:
                edited_lines.append('id="아이디 변경 변수 넣기"')
            if 'pwd' in line:
                edited_lines.append('pwd="비밀번호 넣기"')
            else:
                edited_lines.append(line)
    with open(zepetoInfo,'w') as f:
        f.writelines(edited_lines)



#api testing data
@app.route('/data')
def User_data():
    return {
        'Name' : "hello",
        'Age' : "22",
        "Date" : "x",
        "Cost" : "1000",
    }

@app.route('/rendering')
def Rendering():
    autoprocess = AutoProcess()
    try:
        autoprocess.main()
        return "all ok"
    except:
        return "error occured"



if __name__ == '__main__':
    app.run(debug=True)


