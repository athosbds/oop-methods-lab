# Filtre e classifique produtos pelo faturamento (preço x quantidade) usando list comprehensions.
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

level_faturamento = [
   f"{product['produto']} - ALTO FATURAMENTO" 
   if product["preco"] * product["quantidade"] > 3000
   else f"{product['produto']} - FATURAMENTO NORMAL"
   for product in vendas

]
print(f'NÍVEL DE FATURAMENTO:')
for level in level_faturamento:
    print(level)
print('\nPRODUTOS FATURAMENTOS ALTOS:')
for product in novas_vendas:
    print(f'Produto: {product}')
