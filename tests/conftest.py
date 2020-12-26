import pytest
import os
import sys
import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from app import create_app


@pytest.fixture()
def client():
    my_app = create_app()
    my_app.config['TESTING'] = True
    with my_app.test_client() as client:
        yield client


@pytest.fixture()
def auth_client():
    my_app = create_app()
    my_app.config['TESTING'] = True
    with my_app.test_client() as client:
        with client.session_transaction() as sess:
            sess['authenticated'] = True
        yield client
