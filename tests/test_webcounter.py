import pytest

from webcounter.__main__ import app as flask_app


@pytest.fixture()
def app():
    app = flask_app
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_main_page(client):
    response = client.get("/")
    print(response)
    assert b"<h2>You have seen this" in response.data
