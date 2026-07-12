def validate_user_data(data , require_username = True):
    username = data.get("username")
    password = data.get("password")
    if require_username:
        return None , {"message":"missing credentials"},400
    return{
        "username":username ,
        "password":password
    } , None , None