from services.premium_account_service import PremiumAccount
from flask import jsonify , request , Blueprint
premium_bp = Blueprint("premium_bp", __name__)
premium_account = PremiumAccount()
@premium_bp.route("/premium" , methods = ["POST"])
def create_premium_account_route():
    response , status = premium_account.create_premium_account_service(request.json)
    return jsonify(response), status
@premium_bp.route("/premium" , methods = ["GET"])
def list_premium_accounts():
    response , status = premium_account.list_all_premium_accounts_service()
    return jsonify(response) , status
@premium_bp.route("/premium/<account_number>" , methods = ["PUT"])
def update_premium_account(account_number):
    response , status = premium_account.update_premium_account_service(request.json , account_number)
    return jsonify(response) , status
@premium_bp.route("/premium/account_number/<account_number>" , methods = ["GET"])
def get_one_premium_account(account_number):
    response , status = premium_account.get_one_premium_account_service(account_number)
    return jsonify(response) , status
@premium_bp.route("/premium/<account_number>" , methods = ["DELETE"])
def delete_premium_account(account_number):
    response , status = premium_account.delete_premium_account_service(account_number)
    return jsonify(response) , status
@premium_bp.route("/premium/national_id/<national_id>" , methods = ["GET"])
def get_premium_by_nationalid(national_id):
    response , status = premium_account.search_by_premium_account_by_national_id_service(national_id)
    return jsonify(response) , status
