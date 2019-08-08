#Import needed libs
from flask import Blueprint, request
import json

#Import needed query routes
from querys.authentication import loginUser, logoutUser

#Import wraps for routes
from endpoints.wrappers import wrapLoginRequired

#Create blueprint
authentication = Blueprint('authentication', __name__)

@authentication.route('/login', methods=['POST'])
def login():
    """
    A route to login a user
    """
    return loginUser(request.json)

@authentication.route('/logout/<username>', methods=['GET'])
@wrapLoginRequired
def logout(username):
    """
    A route to logout a user
    """
    return logoutUser(username)