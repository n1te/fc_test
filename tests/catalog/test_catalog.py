def test_article_add_record(article):
    article.add_record({'field1': 'value1', 'field2': 'value2'})
    assert article._common_fields == {'field1': 'value1', 'field2': 'value2'}
    assert article._variations == [{'field1': 'value1', 'field2': 'value2'}]

    article.add_record({'field1': 'value1', 'field2': 'different_value2'})
    assert article._common_fields == {'field1': 'value1'}
    assert article._variations == [
        {'field1': 'value1', 'field2': 'value2'},
        {'field1': 'value1', 'field2': 'different_value2'},
    ]


def test_article_to_dict(article):
    article.add_record({'field1': 'value1', 'field2': 'value2', 'field3': 'value3'})
    article.add_record({'field1': 'value1', 'field2': 'different_value2', 'field3': 'value3'})

    assert article.to_dict(exclude_fields={'field3'}) == {
        'article_number': '12345',
        'field1': 'value1',
        'variations': [{'field2': 'value2'}, {'field2': 'different_value2'}],
    }


def test_catalog_add_record(catalog, record1, record2):
    catalog.add_record(record1)
    assert catalog._common_fields == {'field1': 'value1', 'field2': 'value2'}
    assert '12345' in catalog._articles
    assert catalog._articles['12345']._variations == [{'field1': 'value1', 'field2': 'value2'}]

    catalog.add_record(record2)
    assert catalog._common_fields == {'field1': 'value1'}


def test_catalog_to_dict(catalog, record1, record2, record3):
    catalog.add_record(record1)
    catalog.add_record(record2)
    catalog.add_record(record3)

    result = catalog.to_dict()
    expected_result = {
        'field1': 'value1',
        'articles': [
            {'article_number': '12345', 'variations': [{'field2': 'value2'}, {'field2': 'different_value2'}]},
            {
                'article_number': '67890',
                'field2': 'different_value2',
                'variations': [{}],
            },
        ],
    }
    assert result == expected_result
