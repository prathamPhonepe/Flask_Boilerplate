from utils.responses.responses import  failure_responses
import re


def register_validator(data):
    
    if not data :
         return False
    
    if not "email" in data or not "password" in data :
        return "email and password are required"
        
    email = data["email"]
    password = data["password"]

    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        failure_responses(400, "Invalid email format")
        return "invalid email format"

    password_regex = r'^.{6,20}$'
    if not re.match(password_regex, password):
        return "password char must be atleast 6 char and max must be 20 char long"


    return True