import os
from dotenv import load_dotenv
from flask import Flask, render_template


app = Flask(__name__)

# set path for environment variables file
load_dotenv(dotenv_path='.env')

# config your host & port for app using environment variables
HOST = os.environ['HOST']
PORT = os.environ['FRONTEND_PORT']


# define all routes

# landing page
@app.route('/')
def index():
    return render_template('index.html')


# homepage
@app.route('/home')
def home():
    return render_template('homepage.html')


# Trust House API information page
@app.route('/trutshouse/api/info')
def trusthouse_api_info():
    return render_template('trustHouseAPI.html')


# create a new review
@app.route('/new-review')
def new_review():
    return render_template('writeReviewPage.html')



if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)