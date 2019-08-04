#Import needed Python libraries
import secrets


#Import needed utilities 
from utilities import getHashedPassword, verify_password


def loginUser(login_info):
    """
    Will login a user to the system
    """
    try:
        username = login_info['username']
        password = login_info['password']

        #Function to 
        #   verify user
        #   set token 
        #   Give a result
        #verified, token, level, status, result = verify_user_login(username, password)
        result = "User logged in succesfully"
        verified = True
        level = 'User'
        status = "success"

        if verified:
            token = secrets.token_hex(20)
            #Add token to database for user
            login_dict = {
                "status": status,
                "result": result,
                "username": username,
                "token": token,
                "auth_level": level
            }
        else:
            login_dict = {
                "status": status,
                "username": username,
                "result": result
            }
    except Exception as e:
        login_dict = {
            "status": "error",
            "reason": str(e)
        }
    return login_dict


def logoutUser(username):
    """
    A function to log a user out
    """
    try:
        #Function here to 
            #Delete token in database
            # ...
        logout_dict = {
            "status": "User Successfully Logged Out",
            "username": username
        }
    except:
        logout_dict = {
            "status": "Error",
            "username": username
        }
    return logout_dict