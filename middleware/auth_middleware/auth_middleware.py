
from flask import request, jsonify
from utils.auth.auth_utils import validate_token
from utils.responses.responses import failure_responses
def auth_middlewear(handler):
    print(handler , "this is the handler")
    def wrapper(*args, **kwargs):
        print("middleware triggered") 
        req_header = request.headers
        if not validate_token(req_header):
            return failure_responses(401, "Unauthorized or Invalid Token")
        return handler(*args, **kwargs)

    return wrapper


