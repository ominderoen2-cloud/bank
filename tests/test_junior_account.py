from datetime import datetime
def get_headers(client):
    client.post(
        "/register",
        json={
            "username": "tester",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": "tester",
            "password": "password123"
        }
    )

    token = response.json["access_token"]

    return {
        "Authorization": f"Bearer {token}"}


def test_create_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    response = client.post("/junior", json=payload , headers=headers)

    assert response.status_code == 201


def test_duplicate_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    client.post("/junior", json=payload , headers = headers)
    response = client.post("/junior", json=payload, headers =headers)

    assert response.status_code == 409


def test_list_junior_accounts(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    client.post("/junior", json=payload , headers=headers)

    response = client.get("/junior" , headers=headers)

    assert response.status_code == 200


def test_get_one_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    client.post("/junior", json=payload , headers=headers)

    response = client.get("/junior/account_number/J1", headers=headers)

    assert response.status_code == 200


def test_search_by_birth_certificate(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    client.post("/junior", json=payload , headers = headers)

    response = client.get("/junior/birth_certificate/BC1", headers=headers)

    assert response.status_code == 200


def test_update_junior_account(client):
    payload = {
        "account_number": "J1",
        "birth_certificate_number": "BC1",
        "guardian_id": "12345678",
        "name": "Junior",
        "age": 12,
        "amount": 1000,
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    client.post("/junior", json=payload , headers = headers)

    response = client.put(
        "/junior/J1",
        json={
            "guardian_id": "87654321",
            "name": "Junior Updated",
            "age": 13,
            "amount": 2000,
            "next_of_kin": "Mother"
        },headers=headers
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
        "next_of_kin": "Parent",
        "account_type": "junior_account"
    }
    headers = get_headers(client)

    client.post("/junior", json=payload , headers=headers)

    response = client.delete("/junior/J1", headers=headers)

    assert response.status_code == 200