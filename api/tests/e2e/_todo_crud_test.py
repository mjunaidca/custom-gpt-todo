from fastapi.testclient import TestClient
import pytest
import requests

# Prep to import the app fastapi object and create a test client
import sys
from pathlib import Path

# *\ Import to Get SQLLCHEMY Base class for DB Schema Creation and Migrations
# Determine the directory of the current file (env.py)
current_dir = Path(__file__).resolve().parent

# Add the grand grandparent directory ... (the root of your FastAPI application) to sys.path
sys.path.append(str(current_dir.parent.parent.parent))

# Now you can use relative imports
from api.index import app

client = TestClient(app)

# Test integration and interaction of your FastAPI application with the database and service layer.


# test to get all todos
def test_read_all_todos():
    response = client.get("api/todos/")
    assert response.status_code == 200


def test_create_todo():
    response = client.post(
        "/api/todos/",
        json={
            "title": "Test TODO",
            "description": "Test TODO Description",
            "completed": False
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test TODO"
    assert data["description"] == "Test TODO Description"
    assert data["completed"] == False


def test_get_todo_by_id():
    # Create a todo
    response = client.post(
        "api/todos/",
        json={
            "title": "Test TODO",
            "description": "Test TODO Description",
            "completed": False
        }
    )
    todo_id = response.json()["id"]

    # Get the todo by its ID
    response = client.get(f"api/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["title"] == "Test TODO"
    assert response.json()["description"] == "Test TODO Description"
    assert response.json()["completed"] == False

    # Cleanup
    client.delete(f"api/todos/{todo_id}")


def test_update_todo():
    # Create a todo
    response = client.post(
        "api/todos/",
        json={
            "title": "Test TODO",
            "description": "Test TODO Description",
            "completed": False
        }
    )
    todo_id = response.json()["id"]

    # Update the todo
    response = client.put(
        f"api/todos/{todo_id}",
        json={
            "title": "Updated TODO",
            "description": "Updated TODO Description",
            "completed": True
        }
    )
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["title"] == "Updated TODO"
    assert response.json()["description"] == "Updated TODO Description"
    assert response.json()["completed"] == True

    # Cleanup
    client.delete(f"api/todos/{todo_id}")
