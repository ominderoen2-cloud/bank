def validate_premium_account_data(data , require_national_id= True):
    account_number = data.get("account_number")
    national_id = data.get("national_id")
    name = data.get("name")
    age = data.get("age")
    amount = data.get("amount")
    next_of_kin = data.get("next_of_kin")
    account_type = data.get("account_type")
    if  require_national_id:
        if not account_number or not account_type or not name or not age or not amount or not next_of_kin or national_id is None:
            return None ,{"message":"missing credentials"},400
        try:
          amount = int(amount)
          age = int(age)
        except ValueError:
            return None , {"message":"age and amount must be numbers"},400
    return {
        "account_number":account_number,
        "national_id":national_id ,
        "name":name,
        "age":age ,
        "amount":amount,
        "next_of_kin":next_of_kin ,
        "account_type":account_type

    } , None , None