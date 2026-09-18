import pytest

from todo_store import TodoStore


def test_add_creates_todo():
    store = TodoStore()

    assert store.add("buy milk") == {
        "id": 1,
        "title": "buy milk",
        "done": False,
    }


def test_ids_increase():
    store = TodoStore()
    store.add("first")

    assert store.add("second") == {
        "id": 2,
        "title": "second",
        "done": False,
    }


def test_list_returns_todos():
    store = TodoStore()
    first = store.add("first")
    second = store.add("second")

    assert store.list() == [first, second]


def test_get_returns_todo_or_none():
    store = TodoStore()
    todo = store.add("task")

    assert store.get(1) == todo
    assert store.get(99) is None


def test_set_done_updates_todo_or_returns_none():
    store = TodoStore()
    store.add("task")

    assert store.set_done(1, True) == {
        "id": 1,
        "title": "task",
        "done": True,
    }
    assert store.set_done(99, True) is None


def test_delete_removes_todo_or_returns_false():
    store = TodoStore()
    store.add("task")

    assert store.delete(1) is True
    assert store.get(1) is None
    assert store.delete(99) is False


def test_add_rejects_empty_titles():
    store = TodoStore()

    with pytest.raises(ValueError):
        store.add("")

    with pytest.raises(ValueError):
        store.add("   ")
