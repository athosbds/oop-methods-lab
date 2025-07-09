# Consuma a API e mostre nome, email, empresa e extremos geográficos (norte, sul, leste, oeste)
import requests
url = "https://jsonplaceholder.typicode.com/users"
url_data = requests.get(url)
if url_data.status_code == 200:
    data = url_data.json()
    data_geo = [
        {
            'nome': user['name'],
            'cidade': user['address']['city'],
            'email': user['email'],
            'empresa': user['company']['name'],
            'lat': float(user['address']['geo']['lat']),
            'lng': float(user['address']['geo']['lng'])
        }
        for user in data
    ]
    print('----------------- Dados Usuários -----------------')
    for user in data_geo:
        nome = user['nome']
        email = user['email']
        empresa = user['empresa']
        print(f"""
        Nome: {nome} - Email: {email} - Empresa: {empresa}""")
    south = data_geo[0]
    north = data_geo[0]
    east = data_geo[0]
    west = data_geo[0]
    for user in data_geo:
        if user['lat'] > north['lat']:
            north = user
        if user['lat'] < south['lat']:
            south = user
        if user['lng'] > east['lng']:
            east = user
        if user['lng'] < west['lng']:
            west = user
    print(f"""\n
    NORTE: {north['nome']} - {north['lat']}
    SUL: {south['nome']} - {south['lat']}
    LESTE: {east['nome']} - {east['lng']}
    OESTE: {west['nome']} - {west['lng']}""")
else:
    print(f'Erro ao Acessar API.')