def test_register_creates_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "Hina@X.com", "full_name": "Hina", "password": "hina12345"},
    )
    assert response.status_code == 201
    body = response.json()
    assert body["email"] == "hina@x.com"
    assert "password" not in body
    assert "hashed_password" not in body


def test_register_duplicate_email_returns_409(client):
    payload = {"email": "hina@x.com", "full_name": "Hina", "password": "hina12345"}
    first = client.post("/auth/register", json=payload)
    assert first.status_code == 201

    second = client.post("/auth/register", json={**payload, "email": "HINA@x.com"})
    assert second.status_code == 409


def test_register_short_password_returns_422(client):
    response = client.post(
        "/auth/register",
        json={"email": "hina@x.com", "full_name": "Hina", "password": "123"},
    )
    assert response.status_code == 422
