from fastapi.testclient import TestClient
from fastapi import FastAPI
from authenticator import authenticator
from routers.dairies_routers import router
from bson import ObjectId


app = FastAPI()
app.include_router(router)


def mock_get_current_account_data():
    return {"id": "test_account_id", "username": "testuser"}


app.dependency_overrides[authenticator.get_current_account_data] = mock_get_current_account_data


client = TestClient(app)


valid_test_id = str(ObjectId())


def test_add_dairy():
    response = client.post("/api/dairies/dairies", json={
        "name": "Test Dairy",
        "cost": "2.99",
        "expiration_date": "2023-01-01",
        "measurement": "L",
    })
    assert response.status_code == 200 or 201
    data = response.json()
    assert data["name"] == "Test Dairy"


def test_get_all_Dairies():
    response = client.get("/api/dairies/dairies/mine")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_dairy():
    item_id = valid_test_id
    response = client.put(f"/api/dairies/dairies/{item_id}", json={
        "name": "Updated Test Dairy",
        "cost": "3.99",
        "expiration_date": "2023-02-01",
        "measurement": "L",
    })
    assert response.status_code == 200 or response.status_code == 404


def test_get_dairy():
    item_id = valid_test_id
    response = client.get(f"/api/dairies/{item_id}")
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


def test_delete_dairy():
    item_id = valid_test_id
    response = client.delete(f"/api/dairies/dairies/{item_id}")
    assert response.status_code in [200, 404]
