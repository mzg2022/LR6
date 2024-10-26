import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import decimal

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class CurrenciesList(metaclass=SingletonMeta):
    def __init__(self, request_interval=1):
        self.request_interval = request_interval
        self.last_request_time = datetime.now() - timedelta(seconds=request_interval)

    def get_currencies(self, currencies_ids_lst):
        current_time = datetime.now()
        if (current_time - self.last_request_time).total_seconds() < self.request_interval:
            raise Exception(f"Запрос можно отправлять не чаще, чем раз в {self.request_interval} секунд.")

        self.last_request_time = current_time
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ET.fromstring(response.content)
        result = []

        for currency_id in currencies_ids_lst:
            valute = next((v for v in root.findall("Valute") if v.get('ID') == currency_id), None)
            if len(valute) > 0:
                name = valute.find('Name').text
                value_str = valute.find('Value').text.replace(',', '.')
                integer, fractional = value_str.split('.')
                value_decimal = (decimal.Decimal(integer), decimal.Decimal(fractional))
                char_code = valute.find('CharCode').text
                result.append({char_code: (name, value_decimal)})
            else:
                result.append({currency_id: None})
        return result
