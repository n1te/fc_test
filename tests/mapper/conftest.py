import pytest

from app.mapper import CombineMappingRule, ConcatMappingRule, Mapper


@pytest.fixture
def simple_mapping_rule():
    rule = CombineMappingRule('src', 'dst')
    rule.add_value('src_val', 'dst_val')
    return rule


@pytest.fixture
def combine_mapping_rule():
    rule = CombineMappingRule(['src1', 'src2'], 'dst_combined')
    rule.add_value(['src_val1', 'src_val2'], 'dst_combined_val')
    return rule


@pytest.fixture
def concat_mapping_rule():
    return ConcatMappingRule(['src3', 'src4'], 'dst_concat')


@pytest.fixture
def mapper(simple_mapping_rule, combine_mapping_rule, concat_mapping_rule):
    return Mapper([simple_mapping_rule, combine_mapping_rule, concat_mapping_rule])
