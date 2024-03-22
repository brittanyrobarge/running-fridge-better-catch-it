from fastapi.testclient import TestClient
from fastapi import FastAPI, Depends
from authenticator import authenticator
from routers.produce_routers import router
from bson import ObjectId
import pytest

app = FastAPI()
app.include_router(router)

def mock_get_current_account_data():
    return {"id": "test_account_id", "username": "testuser"}

app.dependency_overrides[authenticator.get_current_account_data] = mock_get_current_account_data

client = TestClient(app)

valid_test_id = str(ObjectId())


def test_add_produce():
    response = client.post("/api/produce/produce", json={
        "name": "Test produce",
        "cost": "2.99",
        "expiration_date": "2023-01-01",
        "measurement": "L",
    })
    assert response.status_code == 200 or 201
    data = response.json()
    assert data["name"] == "Test produce"

def test_get_all_produce():
    response = client.get("/api/produce/produce/mine")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_produce():
    item_id = valid_test_id
    response = client.put(f"/api/produce/produce/{item_id}", json={
        "name": "Updated Test produce",
        "cost": "3.99",
        "expiration_date": "2023-02-01",
        "measurement": "L",
    })
    assert response.status_code == 200 or response.status_code == 404

def test_get_produce():
    item_id = valid_test_id
    response = client.get(f"/api/produce/{item_id}")
    if response.status_code == 404:
        assert response.status_code == 404
    else:
        assert response.status_code == 200
        data = response.json()
        assert 'id' in data
        assert 'name' in data
        assert 'cost' in data
        assert 'expiration_date' in data
        assert 'measurement' in data


def test_delete_produce():
    item_id = valid_test_id
    response = client.delete(f"/api/produce/produce/{item_id}")
    assert response.status_code in [200, 404]
