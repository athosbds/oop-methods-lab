import requests

url = 'https://fakestoreapi.com/products'
get_url = requests.get(url)
if get_url.status_code == 200:
    date = get_url.json()
    filter_stock = [
        stock 
        for stock in date
        if stock['rating']['count'] > 0
    ]
else:
    print('Erro ao acessar a API')

print(f'Produtos com estoque acima de 0')
if filter_stock:
    for product, name in enumerate(filter_stock, start=1):
        title = name['title']
        