vendas = [
    {"produto": "notebook", "preco": 3500, "quantidade": 2},
    {"produto": "mouse", "preco": 150, "quantidade": 10},
    {"produto": "monitor", "preco": 1200, "quantidade": 3},
    {"produto": "teclado", "preco": 200, "quantidade": 5},
    {"produto": "HD", "preco": 500, "quantidade": 1}
]

novas_vendas = [
   product["produto"] for product in vendas
   if product['preco'] * product['quantidade'] > 2000
]

print(novas_vendas)