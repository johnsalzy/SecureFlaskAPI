#Import needed libs
from functools import wraps

#Import our made utilities
from utilities import checkUserLoggedIn
from utilities import checkUserAccessLevel

def wrapLoginRequired(f):
    """
    Will make a route require the user to be logged in
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        username = kwargs['username']
        if checkUserLoggedIn(username):
            return f(*args, **kwargs)
        else:
            return 'Must be logged in to do this function'
    return wrap

def checkUserAccess(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        access_types = [None, 'Basic', 'Moderater', 'Admin', 'SuperAdmin']
        username = kwargs['username']
        wanted_access_level = kwargs['level']
        actual_level = checkUserAccessLevel(username)
        if actual_level == None:
            return "Not sufficient privlidges"
        elif wanted_access_level == actual_level:
            return f(*args, **kwargs)
        elif wanted_access_level != actual_level:
            #Check if user has higher privlidge
            return "Not sufficient privlidges"
        else:
            return "Not sufficient privlidges"


    return wrap