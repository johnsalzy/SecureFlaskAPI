#Import needed libs
from flask import Blueprint, request
from functools import wraps
import json

#Import needed query routes
from querys.authentication import loginUser, logoutUser

#Create blueprint
authentication = Blueprint('authentication', __name__)

def wrapLoginRequired(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if True:
            return f(*args, **kwargs)
        else:
            return 'Must be logged in to do this function'

    return wrap


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