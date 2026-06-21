def test_login(client):
    response = client.post("/auth/login?username=testuser&password=pw")
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_logout(client):
    response = client.post("/auth/logout")
    assert response.status_code == 200
    assert response.json()["data"]["message"] == "Successfully logged out"
