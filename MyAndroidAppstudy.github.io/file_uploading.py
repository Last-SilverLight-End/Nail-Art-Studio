import os
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import logging

logger = logging.getLogger('HELLO WORLD')

app = Flask(__name__)
@app.route('/upload')
def upload_file():
    return render_template('Users.jsx')

@app.route('/uploader', methods = ['GET','POST'])
def uploader_file():

    target = os.path.join(app.config['UPLOAD_FOLDER'], 'test')
    logger.info("welcome to upload`")

    f = request.files['file']
    f_name = f.filename

    destination = "/".join([target,f_name])
    f.save(destination)
    response = "file uploaded successfully"
    return response 

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


