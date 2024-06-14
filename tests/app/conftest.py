import os

import pytest

from app.main import App


@pytest.fixture
def app():
    return App('tests/app/csv/mappings.csv')


@pytest.fixture(scope='module', autouse=True)
def cleanup():
    def remove_json_file():
        if os.path.isfile('tests/app/catalog.json'):
            os.remove('tests/app/catalog.json')

    remove_json_file()
    yield
    remove_json_file()
