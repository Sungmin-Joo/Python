
from flask import Flask, render_template, request, jsonify
import os

def Find_dir(root):
    return os.listdir(root)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/download')
def download():
    arr = Find_dir("./update/word")
    data = {}
    for i in arr:
        f = open("./update/word/" + i,'r')
        lines = f.readlines()
        data[i] = lines
        f.close()

    return jsonify(data)

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    return value

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'   

if __name__ == '__main__':
    print('Func_called - main')
    app.run(host="0.0.0.0", port=5000, debug = True)

else:
    print('Func_called - imported')
    