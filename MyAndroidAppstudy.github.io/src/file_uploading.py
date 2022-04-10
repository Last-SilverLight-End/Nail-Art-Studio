import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename

import logging
app = Flask(__name__)
@app.route('/upload')
def upload_file():
    return render_template('Users.jsx')

@app.route('/uploader', methods = ['GET','POST'])
def uploader_file():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)