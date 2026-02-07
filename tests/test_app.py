import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_remove_participant():
    # Sign up a new participant
    email = "testuser@mergington.edu"
    activity = "Chess Club"
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_resp.status_code == 200
    # Check participant is added
    get_resp = client.get("/activities")
    assert email in get_resp.json()[activity]["participants"]
    # Remove participant
    remove_resp = client.delete(f"/activities/{activity}/participants/{email}")
    assert remove_resp.status_code == 200
    # Check participant is removed
    get_resp2 = client.get("/activities")
    assert email not in get_resp2.json()[activity]["participants"]
