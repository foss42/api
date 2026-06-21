def test_humanize_bytes(client):
    response = client.get("/humanize/bytes?num=1024")
    assert response.status_code == 200
    assert "data" in response.json()

def test_humanize_social(client):
    response = client.get("/humanize/social?num=1500")
    assert response.status_code == 200
    assert "data" in response.json()

def test_humanize_rank(client):
    response = client.get("/humanize/rank?num=1")
    assert response.status_code == 200
    assert "data" in response.json()

def test_humanize_time(client):
    response = client.get("/humanize/time?dt=2023-01-01T00:00:00")
    assert response.status_code == 200
    assert "data" in response.json()
