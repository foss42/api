def test_sse_events(client):
    response = client.get("/sse/events/3")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/event-stream; charset=utf-8"
    
    # Check that it streamed 3 events
    content = response.text
    assert "data: event1" in content
    assert "data: event2" in content
    assert "data: event3" in content
