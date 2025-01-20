import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uuid
import bcrypt
from flask import request 
from utils.responses.responses import success_responses, failure_responses
from config.config import getConnection, closeConnection
from utils.validators.validators import register_validator
from utils.auth.auth_utils import create_token , hash_password

def register_user():
    try:
        data = request.get_json(silent=True)
        validatorResponse =  register_validator(data)

        if validatorResponse != True : 
            return failure_responses(400 , validatorResponse)

        if validatorResponse == True:                
            email = data["email"]
            password = data["password"]
            hashed_password = hash_password(password)
            print("this is the hasshed password " , hashed_password)
            connection = getConnection()
            cursor = connection.cursor()
            try:
                user_id = str(uuid.uuid4())
                print(user_id)
                token = create_token(user_id , email)
                
                formData = {
                    "access_token" : token
                }
                
                return success_responses(200, "User registered successfully"  ,formData)
            finally:
                cursor.close()
                closeConnection(connection)
    except Exception as e:
        print(f"Exception occurred: {e}")
        return failure_responses(500, "Internal server error")
    




def login_user():
    try:
        data = request.get_json(silent=True)
        if not data:
            return failure_responses(400, "Invalid input data")

        validatorResponse = register_validator(data)
        if validatorResponse != True:
            return failure_responses(400, validatorResponse)

        email = data["email"]
        password = data["password"]

        connection = getConnection()
        cursor = connection.cursor()

        try:
            # query = "SELECT user_id, password FROM users WHERE email = %s"
            # cursor.execute(query, (email,))
            # result = cursor.fetchone()

            # if not result:
            #     return failure_responses(404, "User not found")

            # user_id, hashed_password = result

            # if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            #     token = create_token(user_id, email)
            #     form_data = {
            #         "access_token": token
            #     }
            #     return success_responses(200, "Login successful", form_data)
            # else:
            #     return failure_responses(401, "Invalid email or password")
            return success_responses(200 , "successfuly logged in" , {"access_token" : "some token is generated based on the email and the user_id and the user_id is generated usibg uuid"})

        except Exception as e:
            print(f"Exception occurred during login: {e}")
            return failure_responses(500, "Internal server error")
        finally:
            cursor.close()
            closeConnection(connection)

    except Exception as e:
        print(f"Exception occurred: {e}")
        return failure_responses(500, "Internal server error")
