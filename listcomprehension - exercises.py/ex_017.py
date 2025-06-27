import requests

url = 'https://fakestoreapi.com/products'
get_url = requests.get(url)
if get_url.status_code == 200:
    date = get_url.json
    