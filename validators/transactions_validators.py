def validate_transactions_data(data , require_transaction_id = False):
    transaction_id = data.get("transaction_id")
    account_from = data.get("account_from")
    account_to = data.get("account_to")
    amount = data.get("amount")
    account_from_balance = data.get("account_from_balance")
    account_to_balance = data.get("account_to_balance")
    transaction_time = data.get("transaction_time")
    if require_transaction_id:
        if not account_from or not account_to or not amount or not account_from_balance or not account_to_balance or not transaction_time or transaction_id is None:
            return None , {"message":"missing fields"},400
        try:
           amount = int(amount)
        except ValueError:
            return None , {"message":"amount must be a number"},400
            
    return{
        "transaction_id":transaction_id,
        "account_from":account_from,
        "account_to":account_to,
        "amount":amount,
        "account_from_balance":account_from_balance,
        "account_to_balance":account_to_balance,
        "transaction_time":transaction_time
    }, None , None




