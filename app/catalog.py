class CommonFieldsMixin:
    _common_fields: dict[str, str] = None

    def _check_common_fields(self, record: dict[str, str]):
        if self._common_fields is None:
            self._common_fields = record.copy()

        for key, value in record.items():
            if key in self._common_fields and self._common_fields[key] != value:
                del self._common_fields[key]


class Article(CommonFieldsMixin):
    _variations: list[dict[str, str]]
    _article_number: str

    def __init__(self, article_number: str):
        self._variations = []
        self._article_number = article_number

    def add_record(self, record: dict[str, str]):
        self._check_common_fields(record)
        self._variations.append(record)

    def to_dict(self, exclude_fields: set[str]):
        result = {'article_number': self._article_number, 'variations': []}
        for field, value in self._common_fields.items():
            if value and field not in exclude_fields:
                result[field] = value

        exclude_fields |= set(self._common_fields.keys())
        for variation in self._variations:
            result['variations'].append({k: v for k, v in variation.items() if k not in exclude_fields})

        return result


class Catalog(CommonFieldsMixin):
    _articles: dict[str, Article]

    def __init__(self):
        self._articles = {}

    def add_record(self, record: dict[str, str]):
        article_number = record.pop('article_number')
        self._check_common_fields(record)
        if article_number not in self._articles:
            self._articles[article_number] = Article(article_number)

        self._articles[article_number].add_record(record)

    def to_dict(self):
        result = {'articles': []}
        for field, value in self._common_fields.items():
            if value:
                result[field] = value

        for article in self._articles.values():
            result['articles'].append(article.to_dict(exclude_fields=set(self._common_fields.keys())))

        return result
