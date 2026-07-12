from datetime import datetime


def test_create_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    response = client.post("/junior", json=payload)

    assert response.status_code == 201


def test_duplicate_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    client.post("/junior", json=payload)
    response = client.post("/junior", json=payload)

    assert response.status_code == 409


def test_list_junior_accounts(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    client.post("/junior", json=payload)

    response = client.get("/junior")

    assert response.status_code == 200


def test_get_one_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    client.post("/junior", json=payload)

    response = client.get("/junior/account_number/J1")

    assert response.status_code == 200


def test_search_by_birth_certificate(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    client.post("/junior", json=payload)

    response = client.get("/junior/birth_certificate/BC1")

    assert response.status_code == 200


def test_update_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    client.post("/junior", json=payload)

    response = client.put(
        "/junior/J1",
        json={
            "guardian_id": "87654321",
            "name": "Junior Updated",
            "age": 13,
            "amount": 2000,
            "next_of_keen": "Mother"
        },
    )

    assert response.status_code == 200


def test_delete_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_keen": "Parent",
        "account_type": "junior_account"
    }

    client.post("/junior", json=payload)

    response = client.delete("/junior/J1")

    assert response.status_code == 200