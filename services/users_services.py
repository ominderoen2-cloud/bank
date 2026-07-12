from validators.users_validators import validate_user_data
from repositories.users import add_users , get_users , delete_user , update_user , get_one_user
class Users():
    def create_user_service(self , data):
        clean_data , error , status = validate_user_data(data)
        if error:
            return error , status
        success = add_users(clean_data["username"] , clean_data["password"])
        if not success :
            return {"message":"user not registered"},400
        return {"message":"user successfully registered"},201
    def get_users_service(self):
        success = get_users()
        return success ,200
    def remove_user_service(self , username):
        success = delete_user(username)
        if not success:
            return {"message":"user not found"},404
        return {"message":"user successfully deleted"},200
    def get_one_user_service(self , username):
        success = get_one_user(username)
        if not success:
            return {"message":"user not found"},404
        return success , 200
    def update_user_service(self , data):
        clean_data , error , status = validate_user_data(data)
        if error :
            return error , status
        success = update_user(clean_data["username"])
        if not success:
            return {"message":"successfully updated"},400
        return {"message":"not updated"},200

