def test_get_country_codes(client):
    response = client.get("/country/codes")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_country_data(client):
    response = client.get("/country/data?code=US")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data

def test_get_country_data_invalid(client):
    response = client.get("/country/data?code=INVALID")
    assert response.status_code == 404

def test_get_country_flag(client):
    response = client.get("/country/flag?code=US")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_country_name(client):
    response = client.get("/country/name?code=US")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_country_officialname(client):
    response = client.get("/country/officialname?code=US")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_country_subdivisions(client):
    response = client.get("/country/subdivisions?code=US")
    assert response.status_code == 200
    assert "data" in response.json()
