import json
import requests
from config import keys


class ConvertationException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, quote, amount):

        if base == quote:
            raise ConvertationException(f'Зачем переводить {keys[base]} в {keys[base]} 🤦🏻')

        try:
            allert = int(amount)
        except ValueError:
            raise ConvertationException('Количество вводиться с помощью ЦИФР, кэп!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertationException(f'Нет валюты {base} в этом списке /value\nты инструкции вообще читаешь?')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertationException(f'Загляни сюда-ка сюда /value,\nвидишь валюту {quote} в списке доступных?')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}')
        total = float(json.loads(r.content)[keys[quote]])
        return total