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
    if request.method == 'POST':
        f= request.files['file']
        f.save(secure_filename(f.filename))
        response = "file uploaded successfully"
        return response
    else:
        return render_template('Users.jsx') 

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


