from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/numbers')
def numbers():
    return str(random.randint(1,6))