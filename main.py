import time
import requests


def get_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + symbol
    response = requests.get(url)
    data = response.json()
    print(data)
    return float(data["price"])


def monitor_price(symbol):
    max_price = 0
    while True:
        price = get_price(symbol)
        if price > max_price:
            max_price = price
        if price < max_price * 0.99:
            difference = 1 - (price / max_price)
            print(f'Цена упала на {round(difference, 2)}% от максимальной цены за последний час')
        time.sleep(60)


if __name__ == '__main__':
    monitor_price("XRPUSDT")
