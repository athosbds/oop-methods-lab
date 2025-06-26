import requests

url = "https://randomuser.me/api/?results=20"
get_url = requests.get(url)

if get_url.status_code == 200:
    date_url = get_url.json()
    users_results = date_url['results']
    oldest_people = [
        user
        for user in users_results
        if user['dob']['age'] >= 18
    ]
    print(f'Pessoas com 18 anos ou +')
    for user in oldest_people:
        print(user)
    print()
    brazilians = [
        user
        for user in oldest_people
        if user['location']['country'] == 'Brazil'
    ]
    if brazilians:
        for init, user in enumerate(brazilians, start=1):
            name = f"{user['name']['first']} {user['name']['last']}"
            age = f"{user['dob']['age']}"
            country = user['location']['country']
            print(f'{init} - Nome: {name} - Idade: {age} - País: {country}')

else:
    print('Erro ao acessar a API.')

