# Installation

*python 3.10 or higher required*

## Venv
```shell
python -m venv .venv
source .venv/bin/activate
```
Or
```shell
pip install virtualenvwrapper
mkvirtualenv app
```
Then
```shell
pip install -r requirements.txt
```

# Running

Run the app:
```shell
python run.py
```

Help:
```shell
python run.py --help
```

# Tests

```shell
make test
```

# Mapping
A combination of a few multiple fields to a new one can be achieved by using "+" in the "source_type" mapping column:
```text
;;price_buy_net+currency;price_buy_net_currency
```

# Notes
This solution loads all content into memory. If we need to process files that do not fit into memory, we can adjust the solution like this:
1. Process the catalog file line by line
2. Determine a level for each field (catalog/article for specific article_number/variation) without saving all variations
3. Process the catalog file line by line again
4. Save each variation into a document-oriented database using structure from (2)
