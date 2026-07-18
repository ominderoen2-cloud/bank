
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
        "Authorization": f"Bearer {token}"
    }
def test_create_transaction(client):
    headers = get_headers(client)
    response = client.post("/trans" , json = {"transaction_id":"TRANS1" , 
                                              "account_from":"J1" , 
                                              "account_to":"P1" , 
                                              "amount":500 , 
                                              "account_from_balance":1000 , 
                                              "account_to_balance":5000 ,
                                                "transaction_time":datetime.now().isoformat()}, headers=headers)
    assert response.status_code == 201
    assert response.json == {"message":"transaction successfully added"}
def test_duplicate_transaction(client):
    payload = {"transaction_id":"TRANS1" , 
                                              "account_from":"J1" , 
                                              "account_to":"P1" , 
                                              "amount":500 , 
                                              "account_from_balance":1000 , 
                                              "account_to_balance":5000 ,
                                                "transaction_time":datetime.now().isoformat()}
    headers = get_headers(client)
                                              
    client.post("/trans" , json = payload , headers=headers)
    response = client.post("/trans" , json=payload , headers=headers)
    assert response.status_code == 409
    assert response.json == {"message":"transaction not added"}
def list_transactions(client):
    headers = get_headers(client)
    client.post("/trans" , json = {"transaction_id":"TRANS1" , 
                                              "account_from":"J1" , 
                                              "account_to":"P1" , 
                                              "amount":500 , 
                                              "account_from_balance":1000 , 
                                              "account_to_balance":5000 ,
                                                "transaction_time":datetime.now().isoformat()}, headers=headers)
    response = client.get("/trans", headers=headers)
    assert response.status_code == 200
    assert response.json["transaction_id"] == "TRANS1"
    assert response.json["account_from"] == "J1"
    assert response.json["account_to"] == "P1"
    assert response.json["amount"] == 500
    assert response.json["account_from_balance"] == 1000
    assert response.json["account_to_balance"] == 5000
def test_get_one_transaction(client):
     headers = get_headers(client)
     client.post("/trans" , json = {"transaction_id":"TRANS1" , 
                                              "account_from":"J1" , 
                                              "account_to":"P1" , 
                                              "amount":500 , 
                                              "account_from_balance":1000 , 
                                              "account_to_balance":5000 ,
                                              "transaction_time":datetime.now().isoformat()} , headers=headers)
     response = client.get("/trans/trans_id/TRANS1", headers=headers)
     assert response.status_code == 200
     assert response.json["transaction_id"] == "TRANS1"
     assert response.json["account_from"] == "J1"
     assert response.json["account_to"] == "P1"
     assert response.json["amount"] == 500
     assert response.json["account_from_balance"] == 1000
     assert response.json["account_to_balance"] == 5000
def test_update_transaction(client):
    headers= get_headers(client)
    client.post("/trans" , json = {"transaction_id":"TRANS1" , 
                                              "account_from":"J1" , 
                                              "account_to":"P1" , 
                                              "amount":500 , 
                                              "account_from_balance":1000 , 
                                              "account_to_balance":5000 ,
                                              "transaction_time":datetime.now().isoformat()}, headers=headers)
    response = client.put("/trans/recieve/TRANS1" ,json = {
    "account_from_balance":1001,
    "account_to_balance":5000,
    "transaction_time":datetime.now().isoformat()}, headers=headers
) 
        
    assert response.status_code == 200
    assert response.json == {"message":"transaction successfully updated"}

def test_list_transactions(client):
    headers = get_headers(client)
    payload = {
        "transaction_id": "TRANS1",
        "account_from": "J1",
        "account_to": "P1",
        "amount": 500,
        "account_from_balance": 1000,
        "account_to_balance": 5000,
        "transaction_time": datetime.now().isoformat()
    }

    client.post("/trans", json=payload, headers=headers)

    response = client.get("/trans", headers=headers)

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["transaction_id"] == "TRANS1"

def test_get_one_transaction(client):
    payload = {
        "transaction_id": "TRANS1",
        "account_from": "J1",
        "account_to": "P1",
        "amount": 500,
        "account_from_balance": 1000,
        "account_to_balance": 5000,
        "transaction_time": datetime.now().isoformat()
    }
    headers = get_headers(client)

    client.post("/trans", json=payload , headers=headers)

    response = client.get("/trans/trans_id/TRANS1", headers=headers)

    assert response.status_code == 200
    assert response.json["transaction_id"] == "TRANS1"
    assert response.json["account_from"] == "J1"
    assert response.json["account_to"] == "P1"
    assert response.json["amount"] == 500

def test_update_transaction(client):
    payload = {
        "transaction_id": "TRANS1",
        "account_from": "J1",
        "account_to": "P1",
        "amount": 500,
        "account_from_balance": 1000,
        "account_to_balance": 5000,
        "transaction_time": datetime.now().isoformat()
    }
    headers = get_headers(client)

    client.post("/trans", json=payload , headers=headers)

    response = client.put(
        "/trans/recieve/TRANS1",
        json={
            "account_from_balance": 1200,
            "account_to_balance": 4800,
            "transaction_time": datetime.now().isoformat()} , headers=headers
        
    )

    assert response.status_code == 200
    assert response.json["message"] == "transaction successfully updated"
    
 
    


