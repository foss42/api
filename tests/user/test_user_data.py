def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_user_by_id(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_get_profile_unauthorized(client):
    response = client.get("/profile")
    assert response.status_code == 401

def test_get_profile_authorized(client):
    # First login to get the token cookie
    login_response = client.post("/auth/login?username=testuser&password=pw")
    token = login_response.json()["access_token"]
    response = client.get("/profile", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "name" in response.json()
