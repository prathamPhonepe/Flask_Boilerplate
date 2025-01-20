import jwt 
from flask import request

from config.constants import constants



key = constants['JWT_SECRET_KEY']

def create_token(user_id , email):
    return jwt.encode({"user_id": user_id , "email" : email}  , key , algorithm="HS256")




def decode_token(reqHeader):
    print(reqHeader)
    token = reqHeader.get("Authorization")
    if not token:
        return None
    token = token.split(" ")[1]

    print("token", token)

    try:
        return jwt.decode(token, key , algorithms=["HS256"])
    except:
        return None
    


def check_token(reqHeader):
    token = reqHeader.get("Authorization")
    if not token:
        return False
    token = token.split(" ")[1]

    try:
        jwt.decode(token, key , algorithms=["HS256"])
        return True
    except:
        return False
    






def validate_token (req_header):
    token = req_header.get("Authorization")
    if not token or not token.startswith("Bearer "):
        return False

    token = token.split(" ")[1]  
    print(token)

    try:
        jwt.decode(token, key , algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return False
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return False





# data =  create_token(12)
# print(data)


# print( "decoded this is " ,decode_token({"Authorization": f"Bearer {data}"}))