# Liste países que começam com "B" e os que falam português usando list comprehension.
import requests
url = "https://restcountries.com/v3.1/all?fields=name,capital,population,languages"
resposta = requests.get(url)
if resposta.status_code == 200:
    paises = resposta.json()
    countries_letterB = [
        country["name"]["common"] for country in paises
        if country["name"]["common"][0] == 'B'
    ]
    print(f'Países com a Letra B\n{countries_letterB}')
    language_portuguese = [
        country["name"]["common"] for country in paises
        if 'languages' in country and "Portuguese" in country["languages"].values()
    ]
    print(f'\nPaíses Língua Portuguesa:\n{language_portuguese}')
else:
    print("Erro ao buscar dados:", resposta.status_code)