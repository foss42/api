import io

def test_io_delay(client):
    response = client.get("/io/delay?wait=1")
    assert response.status_code == 200
    assert "Waited for" in response.json()["data"]

def test_io_delay_too_long(client):
    response = client.get("/io/delay?wait=121")
    assert response.status_code == 400

def test_io_form(client):
    response = client.post("/io/form", data={"text": "hello world", "sep": "-", "times": 2})
    assert response.status_code == 200
    assert response.json()["data"] == "hello-world-hello-world"

def test_io_filesize(client):
    content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
    response = client.post(
        "/io/filesize", 
        content=content, 
        headers={"Content-Type": "image/png"}
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert "size" in data
    assert data["content-type"] == "image/png"

def test_io_img(client):
    content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
    file = io.BytesIO(content)
    response = client.post(
        "/io/img",
        files={"imfile": ("test.png", file, "image/png")},
        data={"token": "test-token"}
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["provided-token"] == "test-token"
    assert data["file-name"] == "test.png"

def test_io_user_create_update(client):
    res_create = client.post("/io/user/create?username=testuser&email=test@test.com&password=pw")
    assert res_create.status_code == 200
    assert res_create.json()["data"]["username"] == "testuser"

    res_update = client.put("/io/user/update?username=testuser&new_email=new@test.com")
    assert res_update.status_code == 200
    assert res_update.json()["data"]["email"] == "new@test.com"
