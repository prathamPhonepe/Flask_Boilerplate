from flask import Blueprint
from controllers.controller import (
    baseRequest, 
    get_data, 
    post_data, 
    echoServer, 
    getDataFromHeaders, 
    generareJwtToken, 
    verifyTokenGenerated , 
    decodeTokenAndReturn , 
    basicConnectionAndRetrival 
)
from controllers.auth_controller.auth_controller import register_user , login_user
from middleware.auth_middleware.auth_middleware import auth_middleware

def init_routes():
    router = Blueprint('api_v1', __name__)
    router.route('/', methods=['GET'])(baseRequest)
    router.route('/data', methods=['GET'])(get_data)
    router.route('/data', methods=['POST'])(post_data)
    router.route('/echo', methods=['POST'])(echoServer)
    router.route('/headers', methods=['GET'])(getDataFromHeaders)
    router.route('/tokenGenerate', methods=['POST'])(generareJwtToken)
    router.route('/verifyToken', methods=['GET'], endpoint='verify_token')(auth_middleware(verifyTokenGenerated))
    router.route('/decodeToken', methods=['GET'], endpoint='decode_token')(auth_middleware(decodeTokenAndReturn))
    router.route('/basicConnection', methods=['GET'])(basicConnectionAndRetrival)
    router.route('/registerUser', methods=['POST'])(register_user)
    router.route('/loginUser', methods=['POST'])(login_user)


    return router
