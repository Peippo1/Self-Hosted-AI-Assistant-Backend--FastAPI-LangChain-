from fastapi.testclient import TestClient
from app.main import app


def test_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "environment" in data