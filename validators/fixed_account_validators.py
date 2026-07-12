def validate_fixed_account_data(data , require_national_id=True):
    account_number = data.get("account_number")
    national_id = data.get("national_id")
    name = data.get("name")
    age = data.get("age")
    amount = data.get("amount")
    next_of_keen = data.get("next_of_keen")
    account_type = data.get("account_type")
    if require_national_id:
        if not account_number or not national_id or not name or not age or not amount or not next_of_keen or account_type is None:
            return None , {"message":"missing fields"} , 400
        try:
         amount = int(amount)
        except ValueError:
           return None , {"message":"amount must be a number"}
    return {
       "account_number":account_number,
        "national_id":national_id,
        "name":name ,
        "age":age , 
        "amount":amount,
        "next_of_keen":next_of_keen,
        "account_type":account_type
    } ,None , None

