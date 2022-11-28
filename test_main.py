import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    print(client)
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"<title>About</title>" in response.data


""" Write your own tests below."""
def test_everything():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"<title>Index</title>" in response.data
        response = test_client.get("/home")
        assert response.status_code == 302
        assert response.location == "/"
        response = test_client.get("/about")
        assert response.status_code == 200
        assert b"<title>About</title>" in response.data

test_everything()