from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_create_account_success():
    account_info = {"username": "test_user", "password": "test_password"}
    response = client.post("/api/auth/accounts", json=account_info)
    assert response.status_code == 200
    assert "access_token" in response.json()
