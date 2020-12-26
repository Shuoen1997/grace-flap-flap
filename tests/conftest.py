import pytest
import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from app import create_app


@pytest.fixture()
def client():
    my_app = create_app()
    my_app.config['TESTING'] = True
    with my_app.test_client() as client:
        yield client
