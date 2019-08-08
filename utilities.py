import hashlib, binascii, os

def getHashedPassword(password):
    """
    Hash a password for storing.
    """
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """
    Verify a stored password against one provided by user
    """
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def checkUserLoggedIn(username):
    """
    Will check the database to see if the user it logged in
    """
    #Check user logged from database
    # If the have a token, they are logged in
    user_logged_in = True
    return user_logged_in


def checkUserAccessLevel(username):
    """
    Given a username will check the users
    access level from the database
    Note: Check README for different 
    types of access levels
    """
    #Check user access level from database
    access_level = 'Basic'
    return access_level
