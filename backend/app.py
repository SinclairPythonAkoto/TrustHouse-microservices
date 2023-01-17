import os
from dotenv import load_dotenv
from flask import Flask, render_template


app = Flask(__name__)

# set path for environment variables file
load_dotenv(dotenv_path='.env')

# config your host & port for app using environment variable
HOST = os.environ['HOST']
PORT = os.environ['BACKEND_PORT']


# define all routes


@app.route('/')
def home():
    return "hello world"


@app.route('/new-review', methods=['POST'])
def new_review():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)