from services.junior_account_services import JuniorAccount
from flask import Blueprint  , request , jsonify
from flask_jwt_extended import jwt_required , get_jwt_identity
junior_bp = Blueprint("junior_bp" , __name__)
junior_service = JuniorAccount()
@junior_bp.route("/junior" , methods = ["POST"])
def create_account():
    print(request.json)
    response , status = junior_service.add_junior_account_service(request.json)
    return jsonify(response) , status
@junior_bp.route("/junior" , methods = ["GET"])
@jwt_required()
def list_accounts():
    response , status = junior_service.list_all_junior_accounts_service()
    return jsonify(response) , status
@junior_bp.route("/junior/<account_number>" , methods = ["PUT"])
def update_account(account_number):
    response , status = junior_service.update_junior_account_service(request.json , account_number)
    return jsonify(response) , status
@junior_bp.route("/junior/<account_number>" , methods = ["DELETE"])
@jwt_required()
def delete_account(account_number):
    response , status = junior_service.remove_junior_account_service(account_number)
    return jsonify(response) , status
@junior_bp.route("/junior/account_number/<account_number>" , methods = ["GET"])
@jwt_required()
def get_one(account_number):
    response , status = junior_service.get_one_junior_account_service(account_number)
    return jsonify(response) , status
@junior_bp.route("/junior/birth_certificate/<birth_certificate_number>" , methods = ["GET"])
@jwt_required()
def get_by_birthcertificate(birth_certificate_number):
    response , status = junior_service.search_junior_account_by_birth_certificate_service(birth_certificate_number)
    return jsonify(response) , status