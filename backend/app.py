import os
from dotenv import load_dotenv
from flask import Flask, render_template, request


app = Flask(__name__)

# set path for environment variables file
load_dotenv(dotenv_path='.env')

# config your host & port for app using environment variable
HOST = os.environ['HOST']
PORT = os.environ['BACKEND_PORT']


# backend for all routes


@app.route('/')
def home():
    return "hello world"


# create a new review
@app.route('/new-review', methods=['POST'])
def new_review():
    return 'Create a new review'


# display all reviews
@app.route('/review/all', methods=['POST'])
def all_reviews():
    return 'Find all reviews'


# display all review locations
@app.route('/review/locations', methods=['POST'])
def find_locations():
    return 'Find all locations'


# display all reviews by rating 
@app.route('/review/rating', methods=['POST'])
def find_by_rating():
    rating = request.form['searchRating']
    return f'Find all reviews with a rating of {rating}'


# 



if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)