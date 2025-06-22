import requests

url = "https://jsonplaceholder.typicode.com/users"
get = requests.get(url)
if get.status_code == 200:
    data = get.json()
    initial_letter = [
        person["name"] for person in data
        if "address" in person and "city" in person["address"] and person["address"]["city"][0] == 'S'
    ]
print('-----------Dados Pessoais-----------')
for person in data:
     if "address" in person and "city" in person["address"]:
        name = person["name"]
        city = person["address"]["city"]
        print(f'{name} - {city}')
print(f'\n-----------Pessoa em Cidade com a Letra S-----------')
for person in initial_letter:
    print(f'{person}')