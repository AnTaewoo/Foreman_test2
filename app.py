from flask import Flask, jsonify, request

from todo_store import TodoStore


def create_app():
    app = Flask(__name__)
    store = TodoStore()

    @app.route("/todos", methods=["GET"])
    def get_todos():
        return jsonify(store.list())

    @app.route("/todos", methods=["POST"])
    def create_todo():
        data = request.get_json(silent=True) or {}
        title = data.get("title")

        if not isinstance(title, str):
            return jsonify({"error": "title is required"}), 400

        if not title.strip():
            return jsonify({"error": "title cannot be empty"}), 400

        return jsonify(store.add(title)), 201

    @app.route("/todos/<int:todo_id>", methods=["PATCH"])
    def update_todo(todo_id):
        data = request.get_json(silent=True) or {}
        done = data.get("done")

        if store.get(todo_id) is None:
            return jsonify({"error": "not found"}), 404

        if not isinstance(done, bool):
            return jsonify({"error": "done must be boolean"}), 400

        return jsonify(store.set_done(todo_id, done))

    @app.route("/todos/<int:todo_id>", methods=["DELETE"])
    def delete_todo(todo_id):
        if not store.delete(todo_id):
            return jsonify({"error": "not found"}), 404

        return "", 204

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
