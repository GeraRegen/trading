import requests
import pandas as pd

cript = '''
        Здравствуй юный трейдер на криптие
    1 - BTC
    2 - ATOM
    3 - AVAX
    4 - DOGE
    5 - ETH
    6 - XLM
    7 - BNB
    8 - DOT
    9 - LINK
    10 - LTC
    11 - APT
    0 - убежать от проблем и скриться от рынка
        И запомни выигрывают единцы
        УДАЧИ!
'''

def calculate_ema(prices, days):
    ema = prices.ewm(span=days, adjust=False).mean()
    return ema

def calculate_macd(prices):
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)
    macd_line = ema_12 - ema_26
    signal_line = calculate_ema(macd_line, 9)
    macd_histogram = macd_line - signal_line
    return macd_line, signal_line, macd_histogram

def calculate_index_strength(prices, volumes):
    index_strength = (prices.diff() * volumes).dropna()
    return index_strength

def vichislenia(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Не удалось получить данные с сервера. Проверьте URL и ваше интернет-соединение.")
        return

    data = response.json()

    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    # Добавляем столбец с объемами торгов
    df['volume'] = [item[1] for item in data['total_volumes']]

    average_price_22 = df['price'].rolling(window=22).mean()
    average_price_9 = df['price'].rolling(window=9).mean()

    ema_22 = calculate_ema(df['price'], 22)
    ema_9 = calculate_ema(df['price'], 9)

    macd_line, signal_line, macd_histogram = calculate_macd(df['price'])

    index_strength = calculate_index_strength(df['price'], df['volume'])

    print("BTC")
    print("Средняя цена за 22 дня:")
    print(average_price_22)
    print("\nСредняя цена за 9 дней:")
    print(average_price_9)
    print("\nEMA за 22 дня:")
    print(ema_22)
    print("\nEMA за 9 дней:")
    print(ema_9)
    print("\nMACD Line:")
    print(macd_line)
    print("\nSignal Line:")
    print(signal_line)
    print("\nMACD Histogram:")
    print(macd_histogram)
    print("\nИндекс силы:")
    print(index_strength)

print(cript)
tr = input("Введите число:")
while tr != '0':
    if tr == '1':
        variant = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '2':
        variant = "https://api.coingecko.com/api/v3/coins/cosmos/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '3':
        variant = "https://api.coingecko.com/api/v3/coins/avalanche-2/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '4':
        variant = "https://api.coingecko.com/api/v3/coins/dogecoin/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '5':
        variant = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '6':
        variant = "https://api.coingecko.com/api/v3/coins/stellar/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '7':
        variant = "https://api.coingecko.com/api/v3/coins/binancecoin/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '8':
        variant = "https://api.coingecko.com/api/v3/coins/polkadot/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '9':
        variant = "https://api.coingecko.com/api/v3/coins/chainlink/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '10':
        variant = "https://api.coingecko.com/api/v3/coins/litecoin/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '11':
        variant = "https://api.coingecko.com/api/v3/coins/aptos/market_chart?vs_currency=usd&days=30&interval=daily"
        vichislenia(variant)

    elif tr == '0':
        break

    else:
        print("Ты чета попутал дядя")

    tr = input("Введите число:")

print("Удачи")
