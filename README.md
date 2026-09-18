# Foreman_test2

## Run

Start the application:

```bash
python app.py
```

The API runs at `http://127.0.0.1:5000`.

Create a todo:

```bash
curl -X POST http://127.0.0.1:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"buy milk"}'
```

Expected response:

```json
{
  "done": false,
  "id": 1,
  "title": "buy milk"
}
```

List todos:

```bash
curl http://127.0.0.1:5000/todos
```

Expected response:

```json
[
  {
    "done": false,
    "id": 1,
    "title": "buy milk"
  }
]
```

Complete the todo:

```bash
curl -X PATCH http://127.0.0.1:5000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'
```

Expected response:

```json
{
  "done": true,
  "id": 1,
  "title": "buy milk"
}
```

Delete the todo:

```bash
curl -X DELETE http://127.0.0.1:5000/todos/1
```

Expected result: HTTP `204 No Content` with an empty body.

## Test

```bash
pytest -q
```
