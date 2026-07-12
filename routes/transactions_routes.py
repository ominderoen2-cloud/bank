from services.transactions_service import Transactions
from flask import Blueprint , request , jsonify
trans_bp = Blueprint("trans_bp" , __name__)
trans_services = Transactions()
@trans_bp.route("/trans" , methods = ["POST"])
def create_trans():
    response , status = trans_services.add_transaction_service(request.json)
    return jsonify(response) , status
@trans_bp.route("/trans" , methods = ["GET"])
def list_trans():
    response , status = trans_services.get_all_transaction_service()
    return jsonify(response) , status
@trans_bp.route("/trans/trans_id/<transaction_id>", methods = ["GET"])
def get_one_trans(transaction_id):
    response , status = trans_services.get_one_transaction_service(transaction_id)
    return jsonify(response) , status
@trans_bp.route("/trans/send/<transaction_id>" , methods = ["PUT"])
def update_send_trans(transaction_id):
    response , status = trans_services.update_send_transaction_service(request.json , transaction_id)
    return jsonify(response) , status
@trans_bp.route("/trans/recieve/<transaction_id>" , methods = ["PUT"])
def update_recieve_trans(transaction_id):
    response , status = trans_services.update_recieve_transaction_service(request.json , transaction_id)
    return jsonify(response) , status
