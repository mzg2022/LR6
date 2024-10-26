from currencies import CurrenciesList
from decorators import ConcreteDecoratorJSON, ConcreteDecoratorCSV
import time

def main():
    # Получаем данные в базовом формате словаря
    currencies = CurrenciesList()
    base_currencies = currencies.get_currencies(['R01035', 'R01335', 'R01700J'])
    print("Base dictionary format:\n", base_currencies)

    time.sleep(1)

    # Получаем данные в формате JSON, обернув базовый класс JSON-декоратором
    json_currencies = ConcreteDecoratorJSON(currencies)
    json_output = json_currencies.get_currencies(['R01035', 'R01335'])
    print("\nJSON format:\n", json_output)

    time.sleep(1)

    # Получаем данные в формате CSV, обернув базовый класс CSV-декоратором
    csv_currencies = ConcreteDecoratorCSV(currencies)
    csv_output = csv_currencies.get_currencies(['R01035', 'R01335'])
    print("\nCSV format:\n", csv_output)

if __name__ == "__main__":
    main()

