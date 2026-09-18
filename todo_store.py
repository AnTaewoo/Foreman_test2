class TodoStore:
    def __init__(self):
        self._todos = {}
        self._next_id = 1

    def add(self, title):
        if not title.strip():
            raise ValueError("title cannot be empty")

        todo = {
            "id": self._next_id,
            "title": title,
            "done": False,
        }
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def list(self):
        return list(self._todos.values())

    def get(self, todo_id):
        return self._todos.get(todo_id)

    def set_done(self, todo_id, done):
        todo = self._todos.get(todo_id)
        if todo is None:
            return None

        todo["done"] = done
        return todo

    def delete(self, todo_id):
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True
