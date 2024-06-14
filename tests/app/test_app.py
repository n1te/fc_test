from json import loads


def test_app(app):
    app.process_catalog('tests/app/csv/pricat.csv', 'tests/app/catalog.json')

    with open('tests/app/catalog.json') as json_file:
        result = loads(json_file.read())

    with open('tests/app/expected_catalog.json') as json_file:
        expected = loads(json_file.read())

    assert result == expected
