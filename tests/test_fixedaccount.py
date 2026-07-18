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
def test_create_fixed_account(client):
    headers = get_headers(client)
    response = client.post("/fixed" , json = {"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"}, headers = headers)
    assert response.status_code == 201
    assert response.json == {"message":"account successfully created"}
def test_duplicate_fixed_account(client):
    payload = {"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"}
    headers = get_headers(client)
    client.post("/fixed" , json = payload , headers = headers)
    response = client.post("/fixed", json = payload , headers = headers)
    assert response.status_code == 409
    assert response.json == {"message":"account not created"}
def test_list_accounts(client):
    headers = get_headers(client)
    client.post("/fixed" , json = {"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"}, headers = headers)
    response = client.get("/fixed", headers = headers)
    assert response.status_code == 200
    assert response.json == [["F1" , "1" ,"roen",34 , 600 , "chatgpt" , "fixed_account"]]
def test_get_one_fixed(client):
    headers = get_headers(client)
    client.post ("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"}, headers = headers)
    response = client.get("/fixed/account_number/F1" , headers = headers)
    assert response.status_code == 200
    assert response.json == ["F1" , "1" ,"roen",34 , 600 , "chatgpt" , "fixed_account"]
def test_update_fixed(client):
    headers = get_headers(client)
    client.post ("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"}, headers = headers)
    response = client.put("/fixed/F1" , json = {"account_number":"F1", "national_id":"1"  , "name":"roen ominde" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"} , headers = headers)
    assert response.status_code == 200
    assert response.json == {"message":"account successfully updated"}
def test_get_by_national_id(client):
    headers = get_headers(client)
    client.post("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"} , headers = headers)
    response = client.get("/fixed/id/1", headers = headers)
    assert response.status_code == 200
    assert response.json == ["F1" , "1" ,"roen",34 , 600 , "chatgpt" , "fixed_account"]
def test_delete_fixed(client):
    headers = get_headers(client)
    client.post("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"} , headers = headers)
    response = client.delete("/fixed/F1" , headers = headers)
    assert response.status_code == 200
    assert response.json == {"message":"account successfully deleted"}
