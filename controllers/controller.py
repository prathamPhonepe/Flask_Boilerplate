from flask import jsonify, request
from utils.responses.responses import success_responses, failure_responses
from config.config import getConnection, closeConnection
from utils.auth.auth_utils import (
    create_token , decode_token)


def get_data():
    data = {"message": "Hello, this is a GET request!"}
    return jsonify(data), 200



def post_data():
    content = request.get_json()
    if content and "name" in content:
        return success_responses(200 , f"Hello, {content['name']}!")
    else:
        return failure_responses(400 , "Name is required")
    



def echoServer ():
    content  = request.get_json()
    print(content)    
    if content and "message" in content :
        return success_responses(200 , content["message"] , content) 
    return failure_responses(400 , "Message is required")
    


def baseRequest () :
    something = {
        "some value " : True , 
        "another value" : False
    }
    print("something", something)
    return success_responses(200 , "Hello, this is a GET request!" , something)



def getDataFromHeaders ():
    headers = request.headers
    auth = headers.get("Authorization")
    print("auth", auth)
    return success_responses(200 , "Headers received"  )



def generareJwtToken():
    content = request.get_json()
    if content and "user_id" in content:
        token = create_token(content["user_id"])
        return success_responses(200 , "Token generated" , {"token" : token})
    else: 
        return failure_responses(400 , "User Id is required")


def verifyTokenGenerated():
    return success_responses(200 , "Token verified" , {"message" : "Token is valid and verified"})




def decodeTokenAndReturn() : 
    print(request.headers)
    print("hello and this is the decoded :" , decode_token(request.headers))
    return success_responses(200 , "Token decoded"  , decode_token(request.headers))



def basicConnectionAndRetrival():
    try : 
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        print(data)
        closeConnection(connection)

        return success_responses(200 , "Data fetched"  , data)
    except:
        return failure_responses(500 , "Connection failed")    
