from services.fixed_account_services import FixedAccount
from flask import jsonify , request , Blueprint
fixed_account = FixedAccount()
fixed_bp = Blueprint("fixed_bp" , __name__)
@fixed_bp.route("/fixed" , methods = ["POST"])
def add_fixed_route():
    response , status = fixed_account.add_fixed_account_service(request.json)
    return jsonify(response) , status
@fixed_bp.route("/fixed/account_number/<account_number>" , methods = ["GET"])
def get_one_fixed_route(account_number):
    response , status = fixed_account.get_one_account_service(account_number)
    return jsonify(response) , status
@fixed_bp.route("/fixed" , methods = ["GET"])
def get_all_fixed_accounts_route():
    response , status = fixed_account.list_all_fixed_accounts_service()
    return jsonify(response) , status
@fixed_bp.route("/fixed/<account_number>" , methods = ["DELETE"])
def delete_fixed_route(account_number):
    response , status = fixed_account.remove_fixed_accounts_service(account_number)
    return jsonify(response), status
@fixed_bp.route("/fixed/id/<national_id>" , methods = ["GET"])
def get_fixed_by_national_id(national_id):
    response , status = fixed_account.search_by_nationalid_service(national_id)
    return jsonify(response) , status
@fixed_bp.route("/fixed/<account_number>" , methods = ["PUT"])
def update_fixed_account_route(account_number):
    response , status = fixed_account.update_fixed_account_service(request.json , account_number)
    return jsonify(response) , status