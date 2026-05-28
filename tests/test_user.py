def test_create_user_hides_password(client):
    response = client.post(
        "/user/",
        json={
            "name": "Alice",
            "email": "alice@example.com",
            "password": "password123",
            "address": "Address 1",
            "phone": 1234567890,
            "code": 101,
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert "password" not in data
    assert data["email"] == "alice@example.com"


def test_create_user_duplicate_email_returns_conflict(client):
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123",
        "address": "Address 1",
        "phone": 1234567890,
        "code": 101,
    }

    first = client.post("/user/", json=payload)
    second = client.post("/user/", json=payload)

    assert first.status_code == 201
    assert second.status_code == 409
    assert second.json()["error"]["message"] == "Email already registered"
