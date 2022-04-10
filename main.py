from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Users')
def Users_info():
    return 'Users information page'


@app.route('/api/upload', methods = ['POST'])
def upload_file():
    file = request.files['file']
    print(file)
    return "done"
if __name__ == '__main__':
    app.run()