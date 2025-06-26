import requests

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
get_url = requests.get(url)

if get_url.status_code == 200:
    date = get_url.json()
    current_price = [
        value
        for value in date
        if value['current_price'] > 50000
    ]
print(f'-----------Criptomoedas acima dos 50 mil doláres-----------')
if current_price:
    for user, date in enumerate(current_price, start=1):
        name = date['name']
        value = date['current_price']
        symbol = date['symbol']
        print(f'Nome: {name}\nValor: {value}\nSímbolo: {symbol}')
