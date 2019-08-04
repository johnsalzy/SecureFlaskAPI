#Import needed libraries
from flask import Flask
from flask import Blueprint, render_template
from dotenv import load_dotenv
import os


#Import needed blueprints
from endpoints.authentication import authentication


#Load .env vars
load_dotenv()

#Setup app
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    #Register blueprints
    app.register_blueprint(authentication, url_prefix='/authentication')

    #Setup app
    app.secret_key = os.urandom(12)
    app.run(port=os.getenv("API_PORT"), host=os.getenv("API_HOST"), debug=True)