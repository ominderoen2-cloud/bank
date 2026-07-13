#bank/services/junior_account_services.py
from validators.junior_account_validators  import validate_junior_account_data
print(validate_junior_account_data)
from repositories.junior_account import create_junior_account , list_junior_accounts , delete_junior_account , search_junior__account_by_biirth_certificate_number , get_one_junior_account , update_junior_account_data
class JuniorAccount:
 def add_junior_account_service(self ,data):
    clean_data , error , status = validate_junior_account_data(data)
    if error:
        return error , status
    success = create_junior_account(clean_data["account_number"] , clean_data["birth_certificate_number"] , clean_data["guardian_id"], clean_data["name"] , clean_data["age"] , clean_data["amount"] , clean_data["next_of_kin"], clean_data["account_type"])
    if not success:
        return {"message":"account not created"},409
    return {"message":"account successfully created"},201
 def list_all_junior_accounts_service(self):
    return list_junior_accounts(),200
 def remove_junior_account_service(self,account_number):
    success = delete_junior_account(account_number)
    if not success :
        return {"message":"account not found"},404
    return {"message":"account successfully deleted"},200
 def get_one_junior_account_service(self ,account_number):
    success = get_one_junior_account(account_number)
    if not success :
        return {"message":"account not found"},404
    return success, 200
 def search_junior_account_by_birth_certificate_service(self ,account_number):
    success = search_junior__account_by_biirth_certificate_number(account_number)
    if not success:
        return {"message":"account not found"},404
    return success,200
 def update_junior_account_service(self ,data, account_number):
    clean_data , error , status = validate_junior_account_data(data , require_birthcertificate=False)
    if error :
        return error , status
    success = update_junior_account_data(clean_data["guardian_id"] , clean_data["name"] , clean_data["age"], clean_data["amount"], clean_data["next_of_kin"], account_number)
    if not success:
        return {"message":"not updated"},400
    return {"message":"successfully updated"},200


    