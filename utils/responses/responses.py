from  flask import jsonify, request



def success_responses(status , message, data=None):
    response = {
        "status": "success",
        "message": message,
        "data": data if data else {}
    }
    return jsonify(response), status


def failure_responses (status , message , data=None ):
    response = {
        "status" : "failure",
        "message" : message,
        "data" : data if data else {}
    }
    return jsonify(response) , status

