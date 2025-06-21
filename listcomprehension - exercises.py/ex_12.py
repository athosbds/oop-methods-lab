import requests

url = "https://restcountries.com/v3.1/all"
resposta = requests.get(url)

if resposta.status_code == 200:
    paises = resposta.json()

    # Sua list comprehension vem aqui ⬇️

else:
    print("Erro ao buscar dados:", resposta.status_code)
