from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "hello world"

@app.route('/testing')
def testing():
    return "testing"