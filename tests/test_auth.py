def test_register_user(client):
    response = client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    assert response.status_code == 201
    assert response.json == {
        "message": "registration sucessfull"
    }
def test_register_duplicate_user(client):
    payload = {
        "username": "testuser",
        "password": "password123"
    }

    first_response = client.post("/register", json=payload)
    second_response = client.post("/register", json=payload)

    assert first_response.status_code == 201
    assert second_response.status_code == 409
    assert second_response.json == {
        "message": "username already exists"
    }
def test_register_missing_credentials(client):
    response = client.post(
        "/register",
        json={
            "username": "testuser"
        }
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "missing fields"
    }
def test_login_user(client):
    client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json
    assert response.json["access_token"]
def test_login_wrong_password(client):
    client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401
    assert response.json == {
        "message": "invalid password"
    }
def test_login_nonexistent_user(client):
    response = client.post(
        "/login",
        json={
            "username": "doesnotexist",
            "password": "password123"
        }
    )

    assert response.status_code == 401
    assert response.json == {
        "message": "invalid credentials"
    }
def test_login_missing_credentials(client):
    response = client.post(
        "/login",
        json={
            "username": "testuser"
        }
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "missing credentials"
    }
def test_register_whitespace_username(client):
    response = client.post(
        "/register",
        json={
            "username": "   ",
            "password": "password123"
        }
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "missing fields"
    }