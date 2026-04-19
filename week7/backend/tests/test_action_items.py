def test_create_complete_list_and_patch_action_item(client):
    payload = {"description": "Ship it"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    item = r.json()
    assert item["completed"] is False
    assert "created_at" in item and "updated_at" in item

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    done = r.json()
    assert done["completed"] is True

    r = client.get("/action-items/", params={"completed": True, "limit": 5, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.patch(f"/action-items/{item['id']}", json={"description": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["description"] == "Updated"


def test_action_item_pagination(client):
    for i in range(15):
        client.post("/action-items/", json={"description": f"Task {i}"})

    r = client.get("/action-items/", params={"limit": 5})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 5
    assert items[0]["description"] == "Task 14"

    r = client.get("/action-items/", params={"skip": 5, "limit": 5})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 5
    assert items[0]["description"] == "Task 9"

    r = client.get("/action-items/", params={"skip": 100, "limit": 5})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 0


def test_action_item_sorting(client):
    for i in range(5):
        client.post("/action-items/", json={"description": f"Task {i}"})

    r = client.get("/action-items/", params={"sort": "created_at"})
    assert r.status_code == 200
    items = r.json()
    assert items[0]["description"] == "Task 0"
    assert items[-1]["description"] == "Task 4"

    r = client.get("/action-items/", params={"sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert items[0]["description"] == "Task 4"
    assert items[-1]["description"] == "Task 0"


def test_action_item_filtering(client):
    for i in range(5):
        client.post("/action-items/", json={"description": f"Task {i}"})

    client.put(f"/action-items/1/complete")
    client.put(f"/action-items/2/complete")

    r = client.get("/action-items/", params={"completed": True})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2
    for item in items:
        assert item["completed"] is True

    r = client.get("/action-items/", params={"completed": False})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 3
    for item in items:
        assert item["completed"] is False


def test_action_item_deletion(client):
    r = client.post("/action-items/", json={"description": "To Delete"})
    assert r.status_code == 201
    item_id = r.json()["id"]

    r = client.delete(f"/action-items/{item_id}")
    assert r.status_code == 204

    r = client.get(f"/action-items/{item_id}")
    assert r.status_code == 404