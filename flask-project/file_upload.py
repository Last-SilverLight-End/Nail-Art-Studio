from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html ')
    
@app.route('/uploader', methods = ['GET','POST'])
def uploader_file():
    f = request.files['file']
    f.save(secure_filename(f.filename))

    
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)