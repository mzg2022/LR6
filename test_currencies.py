import pytest
import time
from currencies import CurrenciesList
from decorators import ConcreteDecoratorJSON, ConcreteDecoratorCSV
import json
import csv

@pytest.fixture
def currencies():
    return CurrenciesList()

def test_get_currencies(currencies):
    time.sleep(1)
    data = currencies.get_currencies(['R01035', 'R01335', 'R01700J'])
    assert isinstance(data, list)
    assert len(data) == 3

def test_json_decorator(currencies):
    decorated_json = ConcreteDecoratorJSON(currencies)
    time.sleep(1)
    data = decorated_json.get_currencies(['R01035', 'R01335'])
    parsed_data = json.loads(data)
    assert isinstance(parsed_data, list)

def test_csv_decorator(currencies):
    decorated_csv = ConcreteDecoratorCSV(currencies)
    time.sleep(1)
    data = decorated_csv.get_currencies(['R01035', 'R01335'])
    reader = csv.reader(data.splitlines())
    rows = list(reader)
    assert rows[0] == ["Currency Code", "Name", "Value"]
    assert len(rows) > 1
