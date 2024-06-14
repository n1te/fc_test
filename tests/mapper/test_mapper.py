def test_mapper(mapper):
    record = {
        'src': 'src_val',
        'src1': 'src_val1',
        'src2': 'src_val2',
        'src3': 'src_val3',
        'src4': 'src_val4',
        'other_field': 'val',
    }
    mapper.transform(record)
    assert record == {
        'dst': 'dst_val',
        'dst_combined': 'dst_combined_val',
        'dst_concat': 'src_val3 src_val4',
        'other_field': 'val',
    }
