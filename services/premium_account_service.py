#bank/services/premium_account_service.py
from validators.premium_account_validators import validate_premium_account_data
from repositories.premium_account import create_premium_account , list_premium_accounts , get_one_premium_account , delete_premium_account_data , update_premium_account_data , search_premium_account_by_national_id
class PremiumAccount:
 def create_premium_account_service(self ,data):
    clean_data , error , status = validate_premium_account_data(data)
    if error:
        return error , status
    success = create_premium_account(clean_data["account_number"] , clean_data["national_id"], clean_data["name"], clean_data["age"], clean_data["amount"], clean_data["next_of_kin"], clean_data["account_type"])
    if not success:
        return {"message":"account not created"},409
    return {"message":"account successfully created"},201
 def update_premium_account_service(self ,data , account_number):
    clean_data , error , status = validate_premium_account_data(data , require_national_id=False)
    if error:
        return error , status
    success = update_premium_account_data(clean_data["name"] , clean_data["age"], clean_data["amount"], clean_data["next_of_kin"],account_number)
    if not success:
        return{"message":"account not updated"},400
    return {"message":"account successfully updated"},200
 def delete_premium_account_service(self ,account_number):
    success = delete_premium_account_data(account_number)
    if not success:
        return {"message":"account not found"},404
    return {"message":"account successfully deleted"},200
 def search_by_premium_account_by_national_id_service(self,national_id):
    success = search_premium_account_by_national_id(national_id)
    if not success:
        return {"message":"account not found"},404
    return success , 200
 def list_all_premium_accounts_service(self):
    return list_premium_accounts(), 200
 def get_one_premium_account_service(self ,account_number):
    success = get_one_premium_account(account_number)
    if not success:
        return{"message":"account not found"},404
    return success,200
