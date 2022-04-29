import os
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import logging
import imghdr
logger = logging.getLogger('HELLO WORLD')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './public'

@app.route('/')
def hello():
    return 'hello!'

@app.route('/api')
def hellos():
    return{
        'hola' : "oh yeah"
    }

def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.route('/uploader', methods = ['GET','POST'])
def uploader_file():
    f = request.files['file']
    f.save(secure_filename(f.filename))

    
    return 'file uploaded successfully'



@app.route('/data')
def User_data():
    return {
        'Name' : "hello",
        'Age' : "22",
        "Date" : "x",
        "Cost" : "1000",
    }


if __name__ == '__main__':
    app.run(debug=True)


