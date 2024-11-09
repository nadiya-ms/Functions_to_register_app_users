# Pre-exercise code
import re

top_level_domains = [
    "org",
    "net",
    "edu",
    "ac",
    "uk",
    "com"
]

special_pwd_signs = """#+~!%$?()/&"'*{}[]^:.,-_"""

registered_users = []

def validate_name(name):
    """ Checks that the name is greater than two characters and is a string data type.

 Args:
    name (str): The inputted name from the user.

 Returns:
    bool: True if the name passes the check, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9]{2,}$'
    return re.match(pattern, name)

def validate_email(email):
    """ Checks that the email address is in a valid format, has a username greater than 1 character, an '@' symbol, and an allowed domain that is in the `top_level_domains` variable.

  Args:
    email (str): The inputted email from the user.

  Returns:
    bool: True if the email passes the checks, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]{2,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False
    
    domain = email.split('.')[-1]
    if domain not in top_level_domains:
        return False
    return True     


def validate_password(password):
    """ Checks that the password is strong enough. It should include a capital letter, a number between 0-9 and be greater than 8 characters.

  Args:
    password (str): The inputted password from the user.

  Returns:
    bool: True if the password passes the checks, False otherwise.
    """
    has_capital = False
    has_number = False 
    has_special_sign = False

    if len(password) < 8:
        return False

    for char in special_pwd_signs:
        if char in password:
            has_special_sign = True

    for char in password:
       if "A" <= char <= "Z":
           has_capital = True
       if "0" <= char <= "9":
           has_number = True
    
    if has_capital and has_number and has_special_sign:
        return True
    else:
        return False
    