from app import create_app


def test_get_todos_returns_empty_list():
    client = create_app().test_client()

    response = client.get("/todos")

    assert response.status_code == 200
    assert response.get_json() == []


def test_post_todos_creates_todo():
    client = create_app().test_client()

    response = client.post("/todos", json={"title": "buy milk"})

    assert response.status_code == 201
    assert response.get_json() == {
        "id": 1,
        "title": "buy milk",
        "done": False,
    }


def test_post_todos_rejects_missing_title():
    client = create_app().test_client()

    response = client.post("/todos", json={})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_post_todos_rejects_empty_title():
    client = create_app().test_client()

    response = client.post("/todos", json={"title": ""})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_patch_todos_updates_done():
    client = create_app().test_client()
    client.post("/todos", json={"title": "task"})

    response = client.patch("/todos/1", json={"done": True})

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "title": "task",
        "done": True,
    }


def test_patch_todos_missing_todo():
    client = create_app().test_client()

    response = client.patch("/todos/1", json={"done": True})

    assert response.status_code == 404
    assert response.get_json() == {"error": "not found"}


def test_delete_todos():
    client = create_app().test_client()
    client.post("/todos", json={"title": "task"})

    response = client.delete("/todos/1")

    assert response.status_code == 204
    assert response.data == b""


def test_delete_todos_missing_todo():
    client = create_app().test_client()

    response = client.delete("/todos/1")

    assert response.status_code == 404
    assert response.get_json() == {"error": "not found"}
