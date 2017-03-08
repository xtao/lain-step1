from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_lain():
    return 'Hello, LAIN!'
