from tests.conftest import create_user


def test_login_returns_access_and_refresh_token(client):
    create_user(client, "auth@example.com")

    response = client.post(
        "/login",
        data={"username": "auth@example.com", "password": "password123"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


def test_refresh_returns_new_access_token(client):
    create_user(client, "refresh@example.com")

    login_response = client.post(
        "/login",
        data={"username": "refresh@example.com", "password": "password123"},
    )
    refresh_token = login_response.json()["refresh_token"]

    response = client.post("/refresh", json={"refresh_token": refresh_token})

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["refresh_token"] == refresh_token
