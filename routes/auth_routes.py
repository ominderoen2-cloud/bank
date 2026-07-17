from flask import Blueprint, request
from services.auth_services import AuthServices
from flask_jwt_extended import get_jwt_identity , jwt_required

auth_bp = Blueprint("auth", __name__)
auth_service = AuthServices()

@auth_bp.route("/register", methods=["POST"])
def register():
    print("REGISTER ROUTE HIT")
    data = request.get_json()
    response, status = auth_service.register(data)
    return response, status

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = auth_service.login(data)
    if isinstance(result, tuple):
        return result
    return result, 200