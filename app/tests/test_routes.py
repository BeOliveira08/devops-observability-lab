from app.main import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_error():
    client = app.test_client()
    response = client.get("/error")
    assert response.status_code == 500

def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")
    assert response.status_code == 200
