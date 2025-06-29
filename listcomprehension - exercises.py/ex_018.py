import requests
url = 'https://jsonplaceholder.typicode.com/users'
get_url = requests.get(url)
if get_url.status_code == 200:
    results = get_url.json()
    company = [
        user 
        for user in results
        if  'LLC' in user['company']['name']
    ]
    numbers = [
        user['phone']
        for user in results
        
    ]
    print('EMPRESAS COM LLC')
    for user, information in enumerate(company, start=1):
        name = information['name']
        company = information['company']['name']
        print(f'Nome: {name}\nEmpresa: {company}')
    print('\nNúmeros Disponíveis')
    for user, number in enumerate(results, start=1):
        name = number['name']
        phone = number['phone']
        print(f'Nome: {name} - {phone}')

else:
    print(f'Erro ao acessar API.')
