def validate_junior_account_data(data, require_birthcertificate=True):
    account_number = data.get("account_number")
    birth_certificate_number = data.get("birth_certificate_number")
    guardian_id = data.get("guardian_id")
    name = data.get("name")
    age = data.get("age")
    amount = data.get("amount")
    next_of_keen = data.get("next_of_keen")
    account_type = data.get("account_type")

    if require_birthcertificate:
        if (
            account_number is None or
            birth_certificate_number is None or
            guardian_id is None or
            name is None or
            age is None or
            amount is None or
            next_of_keen is None or
            account_type is None
        ):
            return None, {"message": "missing fields"}, 400
    else:
        if (
            guardian_id is None or
            name is None or
            age is None or
            amount is None or
            next_of_keen is None
        ):
            return None, {"message": "missing fields"}, 400

    try:
        age = int(age)
        amount = int(amount)
    except (ValueError, TypeError):
        return None, {"message": "age and amount must be numbers"}, 400

    return {
        "account_number": account_number,
        "birth_certificate_number": birth_certificate_number,
        "guardian_id": guardian_id,
        "name": name,
        "age": age,
        "amount": amount,
        "next_of_keen": next_of_keen,
        "account_type": account_type,
    }, None, None