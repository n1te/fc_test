import csv
from json import dumps

from app.catalog import Catalog
from app.mapper import CombineMappingRule, ConcatMappingRule, Mapper


class App:
    mapper: Mapper

    def __init__(self, mappings_file_path: str):
        self.init_mapper(mappings_file_path)

    @staticmethod
    def _get_csv_reader(file_path: str):
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                yield row

    @staticmethod
    def _write_json(file_path: str, data: dict):
        with open(file_path, 'w') as outfile:
            outfile.write(dumps(data, indent=4))

    def init_mapper(self, mappings_file_path: str):
        reader = self._get_csv_reader(mappings_file_path)
        next(reader)
        rules = {}
        for source, destination, source_type, destination_type in reader:
            if '+' in source_type:
                rules[source_type] = ConcatMappingRule(source_type.split('+'), destination_type)
            else:
                if source_type not in rules:
                    rules[source_type] = CombineMappingRule(source_type.split('|'), destination_type)
                rules[source_type].add_value(source.split('|'), destination)

        self.mapper = Mapper(list(rules.values()))

    def process_catalog(self, price_catalog_file_path: str, output_file_path: str):
        reader = self._get_csv_reader(price_catalog_file_path)
        header = next(reader)
        catalog = Catalog()
        for row in reader:
            record = dict(zip(header, row))
            catalog.add_record(self.mapper.transform(record))

        result = catalog.to_dict()

        self._write_json(output_file_path, result)
