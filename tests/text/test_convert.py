def test_to_slug(client):
    response = client.get("/convert/slug?text=hello world")
    assert response.status_code == 200
    assert response.json()["data"] == "hello-world"

def test_phone_number_to_numeric(client):
    response = client.get("/convert/phone2numeric?text=1-800-FLOWERS")
    assert response.status_code == 200
    assert "data" in response.json()

def test_to_leet(client):
    response = client.get("/convert/leet?text=leet")
    assert response.status_code == 200
    assert "data" in response.json()

def test_to_upside_down(client):
    response = client.get("/convert/upsidedown?text=hello")
    assert response.status_code == 200
    assert "data" in response.json()

def test_to_mirror(client):
    response = client.get("/convert/mirror?text=hello")
    assert response.status_code == 200
    assert "data" in response.json()
