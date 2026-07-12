#bank/services/fixed_account_services
from validators.fixed_account_validators import validate_fixed_account_data
from repositories.fixed_account import create_fixed_account , get_one_fixed_account , list_fixed_account , search_fixedaccount_by_national_id , update_fixed_account_data, delete_fixed_account
class FixedAccount:
 def add_fixed_account_service(self,data):
    clean_data , error , status = validate_fixed_account_data(data)
    print(clean_data)
    print(error)
    print(status)
    if error:
        return error , status
    success = create_fixed_account(clean_data["account_number"] , clean_data["national_id"] , clean_data["name"] , clean_data["age"] , clean_data["amount"],clean_data["next_of_keen"] , clean_data["account_type"])
    if not success:
        return {"message":"account not created"},409
    return {"message":"account successfully created"},201
 def list_all_fixed_accounts_service(self):
    return list_fixed_account(),200
 def remove_fixed_accounts_service(self ,account_number):
    success = delete_fixed_account(account_number)
    if not success:
        return {"message":"account not found"}, 404
    return {"message":"account successfully deleted"},200
 def get_one_account_service(self ,account_number):
    success = get_one_fixed_account(account_number)
    if not success:
        return {"message":"account not found"},404
    return success, 200
 def search_by_nationalid_service(self ,national_id):
    success = search_fixedaccount_by_national_id(national_id)
    if not success:
        return {"message":"account not found"},404
    return  success, 200
 def update_fixed_account_service(self ,data,account_number):
    clean_data , error , status = validate_fixed_account_data(data)
    if error:
        return error , status
    success = update_fixed_account_data(clean_data["name"] , clean_data["age"] , clean_data["amount"], clean_data["next_of_keen"], account_number)
    if not success:
        return {"message":"account not updated"},400
    return {"message":"account successfully updated"}, 200


