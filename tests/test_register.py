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
