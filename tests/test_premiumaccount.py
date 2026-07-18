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



def test_create_premium_account(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    response = client.post("/premium", json=payload , headers=headers)

    assert response.status_code == 201


def test_duplicate_premium_account(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    client.post("/premium", json=payload , headers=headers)
    response = client.post("/premium", json=payload , headers=headers)

    assert response.status_code == 409


def test_list_premium_accounts(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    client.post("/premium", json=payload, headers=headers)

    response = client.get("/premium", headers=headers)

    assert response.status_code == 200
    assert len(response.json) >= 1


def test_get_one_premium_account(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    client.post("/premium", json=payload , headers=headers)

    response = client.get("/premium/account_number/P1", headers=headers)

    assert response.status_code == 200


def test_search_by_national_id(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    client.post("/premium", json=payload , headers=headers)

    response = client.get("/premium/national_id/12345678" , headers=headers)

    assert response.status_code == 200


def test_update_premium_account(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    client.post("/premium", json=payload , headers=headers)

    response = client.put(
        "/premium/P1",
        json={
            "name": "John Updated",
            "age": 26,
            "amount": 6000,
            "next_of_kin": "James"
        },headers=headers
    )

    assert response.status_code == 200


def test_delete_premium_account(client):
    payload = {
        "account_number": "P1",
        "national_id": "12345678",
        "name": "John",
        "age": 25,
        "amount": 5000,
        "next_of_kin": "Jane",
        "account_type": "premium_account"
    }
    headers = get_headers(client)

    client.post("/premium", json=payload , headers=headers)

    response = client.delete("/premium/P1", headers=headers)

    assert response.status_code == 200