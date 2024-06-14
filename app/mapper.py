import logging

logger = logging.getLogger(__name__)


class MappingRuleBase:
    _source_types: list[str]
    _destination_type: str

    def __init__(self, source_type: list[str] | str, destination_type: str, **params):
        self._source_types = source_type if isinstance(source_type, list) else [source_type]
        self._destination_type = destination_type

    def _extract_source_values(self, record: dict[str, str]) -> list[str]:
        source_values = []
        for source_type in self._source_types:
            try:
                source_values.append(record[source_type])
                del record[source_type]
            except KeyError:
                logger.warning(f'Mapping error: {source_type} is not in {record=}')
        return source_values

    def transform(self, record: dict[str, str]):
        raise NotImplementedError


class CombineMappingRule(MappingRuleBase):
    _values: dict[str, str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._values = {}

    def add_value(self, src_value: list[str] | str, dst_value: str):
        if isinstance(src_value, list):
            src_value = ''.join(src_value)

        self._values[src_value] = dst_value

    def transform(self, record: dict[str, str]):
        source_values = self._extract_source_values(record)
        try:
            record[self._destination_type] = self._values[''.join(source_values)]
        except KeyError:
            logger.warning(
                f'Mapping error: destination value not found for destination_type={self._destination_type}, '
                f'{source_values=}'
            )


class ConcatMappingRule(MappingRuleBase):
    def transform(self, record: dict[str, str]):
        source_values = self._extract_source_values(record)
        record[self._destination_type] = ' '.join(source_values)


class Mapper:
    _rules: list[MappingRuleBase]

    def __init__(self, rules: list[MappingRuleBase]):
        self._rules = rules

    def transform(self, record: dict) -> dict:
        for rule in self._rules:
            rule.transform(record)
        return record
