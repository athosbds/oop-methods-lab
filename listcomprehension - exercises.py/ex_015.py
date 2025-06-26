import requests

url = "https://randomuser.me/api/?results=20"
get_url = requests.get(url)

if get_url.status_code == 200:
    date_url = get_url.json()
    users = date_url['results']
    oldest_people = [
        user
        for user in users
        if user['dob']['age'] >= 18
    ]
    print('Pessoas com 18 anos ou mais:')
    for user in oldest_people:
        name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
        age = user['dob']['age']
        country = user['location']['country']
        print(f'Nome: {name} - Idade: {age} - País: {country}')
    print()
    brazilians = [user for user in users if user['location']['country'] == 'Brazil']
    if brazilians:
        print('Usuários do Brasil:')
        for idx, user in enumerate(brazilians, start=1):
            name = f"{user['name']['first']} {user['name']['last']}"
            age = user['dob']['age']
            print(f'{idx} - Nome: {name} - Idade: {age} - País: Brazil')
    else:
        print('Nenhum usuário do Brasil encontrado.')
else:
    print('Erro ao acessar a API.')
