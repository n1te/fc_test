import pytest

from app.catalog import Article, Catalog


@pytest.fixture
def article():
    return Article(article_number='12345')


@pytest.fixture
def catalog():
    return Catalog()


@pytest.fixture
def record1():
    return {'article_number': '12345', 'field1': 'value1', 'field2': 'value2'}


@pytest.fixture
def record2():
    return {'article_number': '12345', 'field1': 'value1', 'field2': 'different_value2'}


@pytest.fixture
def record3():
    return {'article_number': '67890', 'field1': 'value1', 'field2': 'different_value2'}
