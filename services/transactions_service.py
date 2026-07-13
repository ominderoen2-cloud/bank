#bank/services/transactions_services.py
from validators.transactions_validators import validate_transactions_data
from repositories.transactions import add_transaction , get_all_transactions , get_one_transactions ,update_transaction
class Transactions:
    def add_transaction_service(self ,data):
        clean_data , error , status = validate_transactions_data(data)
        if error :
            return error , status
        success = add_transaction(clean_data["transaction_id"], clean_data["account_from"] , clean_data["account_to"] , clean_data["amount"],clean_data["account_from_balance"],clean_data["account_to_balance"], clean_data["transaction_time"])
        if not success:
            return {"message":"transaction not added"},409
        return{"message":"transaction successfully added"},201
    def get_all_transaction_service(self):
        return get_all_transactions(),200
    def get_one_transaction_service(self,transaction_id):
        success = get_one_transactions(transaction_id)
        if not success:
            return{"message":"transaction not found"},404
        return success , 200
    def update_receive_transaction_service(self, data, transaction_id):
       clean_data, error, status = validate_transactions_data(
          data,
          require_transaction_id=False
         )

       if error:
        return error, status

       success = update_transaction(
        clean_data["account_from_balance"],
        clean_data["account_to_balance"],
        clean_data["transaction_time"],
        transaction_id
    )

       if not success:
        return {"message": "transaction not updated"}, 400

       return {"message": "transaction successfully updated"}, 200