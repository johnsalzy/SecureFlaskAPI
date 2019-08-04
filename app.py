#Import needed libraries
from flask import Flask
from dotenv import load_dotenv
import os

#Load .env vars
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=os.getenv("API_PORT"), host=os.getenv("API_HOST"), debug=True)