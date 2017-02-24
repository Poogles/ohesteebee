import pytest

import ohessteebee.client as client

put_example = {
    "metric": "sys.cpu.nice",
    "timestamp": 1346846400,
    "value": 18,
    "tags": {
       "host": "web01",
       "dc": "lga"
    }
}


@pytest.fixture(autouse=True)
def patch_requests_session(mocker):
    mocker.patch('client.requests.')


@pytest.fixture()
def ostb():
    pass


def test_client():
    pass


def test_get():
    pass


def test_put():
    pass
