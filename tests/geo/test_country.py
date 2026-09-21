def test_get_country_codes(client):
    response = client.get("/country/codes")
    assert response.status_code == 200
    assert "data" in response.json()

def test_filter_country_codes(client):
    response = client.get("/country/filtercodes?country=India&country=US")
    assert response.status_code == 200
    assert response.json()["data"] == {
        "India": "IN",
        "United States of America": "US",
    }

def test_filter_country_codes_uses_word_boundaries(client):
    response = client.get("/country/filtercodes?country=India")
    assert response.status_code == 200
    assert response.json()["data"] == {"India": "IN"}

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
