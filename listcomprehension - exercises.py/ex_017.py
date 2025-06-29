##Enunciado:** Consuma a Fake Store API, liste produtos com estoque maior que zero mostrando nome, categoria e quantidade, e também produtos com avaliação igual ou superior a 4.0 mostrando nome e nota.
import requests

url = 'https://fakestoreapi.com/products'
get_url = requests.get(url)
if get_url.status_code == 200:
    products = get_url.json()
    filter_stock = [
        stock 
        for stock in products
        if stock['rating']['count'] > 0
    ]
    evaluated = [
        rate
        for rate in products
        if rate['rating']['rate'] >= 4.0
    ]
else:
    print('Erro ao acessar a API')

print(f'PRODUTOS ACIMA DE 0 ESTOQUE')
if filter_stock:
    for product, name in enumerate(filter_stock, start=1):
        title = name['title']
        category = name['category']
        count = name['rating']['count']
        print(f'NOME PRODUTO: {title}\nCATEGORIA: {category}\nESTOQUE: {count}')
print('\nPRODUTOS COM NOTAS ALTAS')
if evaluated:
    for product, name in enumerate(evaluated, start=1):
        title = name['title']
        rate = name['rate']
        print(f'PRODUTO: {title}\nNOTA: {rate }')
else:
    print('Estoques não disponíveis.')
        
