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

def test_io_user_patch_delete(client):
    client.post("/io/user/create?username=patchuser&email=patch@test.com&password=pw")
    
    # Test PATCH
    res_patch = client.patch("/io/user/patchuser?new_email=patched@test.com")
    assert res_patch.status_code == 200
    assert res_patch.json()["data"]["email"] == "patched@test.com"
    assert res_patch.json()["data"]["password"] == "pw" # unchanged
    
    # Test DELETE
    res_delete = client.delete("/io/user/patchuser")
    assert res_delete.status_code == 200
    assert res_delete.json()["data"]["message"] == "User deleted successfully"
    
    # Try to PATCH deleted user
    res_patch_after_delete = client.patch("/io/user/patchuser?new_email=patched@test.com")
    assert res_patch_after_delete.status_code == 404

def test_io_head(client):
    response = client.head("/io/head")
    assert response.status_code == 200
    assert response.headers.get("x-custom-head") == "HEAD works"
    assert not response.content

def test_io_octet_stream(client):
    content = b"Binary \x00\x01\x02 Stream"
    response = client.post(
        "/io/octet-stream",
        content=content,
        headers={"Content-Type": "application/octet-stream"}
    )
    assert response.status_code == 200
    assert "size" in response.json()["data"]
    assert response.json()["data"]["message"] == "Octet stream processed successfully"

def test_io_octet_stream_invalid_type(client):
    content = b"Binary \x00\x01\x02 Stream"
    response = client.post(
        "/io/octet-stream",
        content=content,
        headers={"Content-Type": "text/plain"}
    )
    assert response.status_code == 400

