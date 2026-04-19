def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"


def test_note_pagination(client):
    for i in range(15):
        client.post("/notes/", json={"title": f"Note {i}", "content": f"Content {i}"})

    r = client.get("/notes/", params={"limit": 5})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 5
    assert items[0]["title"] == "Note 14"

    r = client.get("/notes/", params={"skip": 5, "limit": 5})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 5
    assert items[0]["title"] == "Note 9"

    r = client.get("/notes/", params={"skip": 100, "limit": 5})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 0


def test_note_sorting(client):
    for i in range(5):
        client.post("/notes/", json={"title": f"Note {i}", "content": f"Content {i}"})

    r = client.get("/notes/", params={"sort": "created_at"})
    assert r.status_code == 200
    items = r.json()
    assert items[0]["title"] == "Note 0"
    assert items[-1]["title"] == "Note 4"

    r = client.get("/notes/", params={"sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert items[0]["title"] == "Note 4"
    assert items[-1]["title"] == "Note 0"

    r = client.get("/notes/", params={"sort": "title"})
    assert r.status_code == 200


def test_note_deletion(client):
    r = client.post("/notes/", json={"title": "To Delete", "content": "Delete me"})
    assert r.status_code == 201
    note_id = r.json()["id"]

    r = client.delete(f"/notes/{note_id}")
    assert r.status_code == 204

    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 404


def test_note_search(client):
    client.post("/notes/", json={"title": "Python Tutorial", "content": "Learn Python"})
    client.post("/notes/", json={"title": "JavaScript Guide", "content": "Learn JS"})
    client.post("/notes/", json={"title": "FastAPI Notes", "content": "Python framework"})

    r = client.get("/notes/", params={"q": "Python"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2

    r = client.get("/notes/", params={"q": "JavaScript"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1
    assert items[0]["title"] == "JavaScript Guide"