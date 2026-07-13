def test_create_fixed_account(client):
    response = client.post("/fixed" , json = {"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    assert response.status_code == 201
    assert response.json == {"message":"account successfully created"}
def test_duplicate_fixed_account(client):
    payload = {"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"}
    client.post("/fixed" , json = payload)
    response = client.post("/fixed", json = payload)
    assert response.status_code == 409
    assert response.json == {"message":"account not created"}
def test_list_accounts(client):
    client.post("/fixed" , json = {"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    response = client.get("/fixed")
    assert response.status_code == 200
    assert response.json == [["F1" , "1" ,"roen",34 , 600 , "chatgpt" , "fixed_account"]]
def test_get_one_fixed(client):
    client.post ("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    response = client.get("/fixed/account_number/F1")
    assert response.status_code == 200
    assert response.json == ["F1" , "1" ,"roen",34 , 600 , "chatgpt" , "fixed_account"]
def test_update_fixed(client):
    client.post ("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    response = client.put("/fixed/F1" , json = {"account_number":"F1", "national_id":"1"  , "name":"roen ominde" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    assert response.status_code == 200
    assert response.json == {"message":"account successfully updated"}
def test_get_by_national_id(client):
    client.post("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    response = client.get("/fixed/id/1")
    assert response.status_code == 200
    assert response.json == ["F1" , "1" ,"roen",34 , 600 , "chatgpt" , "fixed_account"]
def test_delete_fixed(client):
    client.post("/fixed" , json ={"account_number":"F1", "national_id":"1"  , "name":"roen" , "age":34 ,"amount":600 ,"next_of_kin":"chatgpt","account_type":"fixed_account"})
    response = client.delete("/fixed/F1")
    assert response.status_code == 200
    assert response.json == {"message":"account successfully deleted"}

    