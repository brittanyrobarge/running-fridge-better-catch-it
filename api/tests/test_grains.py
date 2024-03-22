from fastapi.testclient import TestClient
from queries.grains_queries import ItemRepository
from main import app

client = TestClient(app=app)


def fake_get_current_account_data():
    return {"id": "FAKE_ACCOUNT_ID"}


class FakeItemRepository:
    def add_grain(self, item, account_id):
        items = item.dict()
        items["account_id"] = account_id
        items["id"] = "FAKE_ID"
        return items


def test_add_grain():
    app.dependency_overrides[ItemRepository] = FakeItemRepository
    item = {
        "name": "string",
        "cost": "string",
        "expiration_date": "2024-03-12",
        "measurement": "string",
        "store_name": "string"
        }
    res = client.post("/api/grains/grains", json=item)
    assert res.status_code == 401


def test_delete_grains():
    app.dependency_overrides[ItemRepository] = FakeItemRepository
    item = {
        "name": "string",
        "cost": "string",
        "expiration_date": "2024-03-12",
        "measurement": "string",
        "store_name": "string"
        }
    res = client.post("/api/grains/grains", json=item)
    assert res.status_code == 401


def test_get_grain():
    app.dependency_overrides[ItemRepository] = FakeItemRepository
    item = {
        "name": "string",
        "cost": "string",
        "expiration_date": "2024-03-12",
        "measurement": "string",
        "store_name": "string"
        }
    res = client.post("/api/grains/grains", json=item)
    assert res.status_code == 401


def test_update_grain():
    app.dependency_overrides[ItemRepository] = FakeItemRepository
    item = {
        "name": "string",
        "cost": "string",
        "expiration_date": "2024-03-12",
        "measurement": "string",
        "store_name": "string"
        }
    res = client.post("/api/grains/grains", json=item)
    assert res.status_code == 401


def test_get_all_for_account():
    app.dependency_overrides[ItemRepository] = FakeItemRepository
    item = {
        "name": "string",
        "cost": "string",
        "expiration_date": "2024-03-12",
        "measurement": "string",
        "store_name": "string"
        }
    res = client.post("/api/grains/grains", json=item)
    assert res.status_code == 401
