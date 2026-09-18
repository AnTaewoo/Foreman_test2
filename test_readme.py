from pathlib import Path


README = Path(__file__).with_name("README.md").read_text()


def test_readme_contains_required_commands_and_sections():
    assert "## Run" in README
    assert "python app.py" in README
    assert "## Test" in README
    assert "pytest -q" in README


def test_readme_contains_required_curl_operations():
    assert "curl -X POST http://127.0.0.1:5000/todos" in README
    assert "curl http://127.0.0.1:5000/todos" in README
    assert "curl -X PATCH http://127.0.0.1:5000/todos/1" in README
    assert "curl -X DELETE http://127.0.0.1:5000/todos/1" in README
