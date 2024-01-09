"""
Unit Tests for TODO CRUD Routes
"""

import requests
import pytest
from unittest.mock import patch, MagicMock, AsyncMock, ANY
from uuid import UUID
from fastapi.testclient import TestClient

import sys
from pathlib import Path

# Prep to import the app fastapi object and create a test client
current_dir = Path(__file__).resolve().parent

# Add the grand grandparent directory ... (the root of your FastAPI application) to sys.path
sys.path.append(str(current_dir.parent.parent.parent))

# Now you can use relative imports
from api.models._user_auth import LoginResonse, UserOutput, UserInDB, RegisterUser
from api.utils._helpers import get_password_hash
from api.index import app


@pytest.fixture
def client():
    return TestClient(app)

# Create Resuable Pytest Fixtures

# @pytest.fixture
# def sample_todo():
#     return TODO(id=UUID("12345678123456781234567812345678"), title="Test TODO", description="This is a test TODO")


# def test_get_all_todo_data(sample_todo):
#     mock_session = Mock(spec=Session)
#     mock_session.query().all.return_value = [sample_todo]

#     with patch('sqlalchemy.orm.Session', return_value=mock_session):
#         result = todos_crud.get_all_todo_data(mock_session)

#     assert result == [sample_todo]
#     mock_session.query.assert_called_with(TODO)
#     mock_session.query().all.assert_called_once()


