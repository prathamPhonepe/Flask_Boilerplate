from  flask import jsonify, request



def success_responses(status , message, data=None):
    response = {
        "message": message,
        "success" : True , 
        "data": data if data else {}
    }
    return jsonify(response), status


def failure_responses (status , message , data=None ):
    response = {
        "success" : False , 
        "message" : message,
        "data" : data if data else {}
    }
    return jsonify(response) , status

