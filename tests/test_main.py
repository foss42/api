def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "data" in response.json()
