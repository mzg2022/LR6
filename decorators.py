import json
import csv
from io import StringIO

class Decorator:
    def __init__(self, component):
        self._component = component

    def get_currencies(self, currencies_ids_lst):
        return self._component.get_currencies(currencies_ids_lst)

class ConcreteDecoratorJSON(Decorator):
    def get_currencies(self, currencies_ids_lst):
        data = self._component.get_currencies(currencies_ids_lst)
        return json.dumps(data, ensure_ascii=False, default=str)

class ConcreteDecoratorCSV(Decorator):
    def get_currencies(self, currencies_ids_lst):
        data = self._component.get_currencies(currencies_ids_lst)
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Currency Code", "Name", "Value"])
        for entry in data:
            for char_code, (name, value) in entry.items():
                writer.writerow([char_code, name, f"{value[0]},{value[1]}"])
        return output.getvalue()
