def test_hello(app_client):
    response = app_client.get("api/users/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_hello_exception(app_client):
    response = app_client.get("api/users/exception")
    assert response.status_code == 500
    assert response.json() == "hoge"
