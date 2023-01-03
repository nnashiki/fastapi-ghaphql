def test_hello(app_client):
    response = app_client.get("super/users")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
