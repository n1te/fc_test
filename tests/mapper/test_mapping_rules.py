def test_simple_mapping_rule(simple_mapping_rule):
    data = {'src': 'src_val'}
    simple_mapping_rule.transform(data)
    assert data == {'dst': 'dst_val'}


def test_combine_mapping_rule(combine_mapping_rule):
    data = {'src1': 'src_val1', 'src2': 'src_val2'}
    combine_mapping_rule.transform(data)
    assert data == {'dst_combined': 'dst_combined_val'}


def test_concat_mapping_rule(concat_mapping_rule):
    data = {'src3': 'src_val3', 'src4': 'src_val4'}
    concat_mapping_rule.transform(data)
    assert data == {'dst_concat': 'src_val3 src_val4'}
