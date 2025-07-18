# Liste os nomes dos usuários com saldo acima de 1000 usando list comprehension.
usuarios = [
    {"id": 1, "nome": "Ana", "saldo": 850},
    {"id": 2, "nome": "Bruno", "saldo": 1250},
    {"id": 3, "nome": "Carlos", "saldo": 3000},
    {"id": 4, "nome": "Diana", "saldo": 500},
]

saldo_alto = [
    user["nome"] for user in usuarios
    if user["saldo"] > 1000
]
print(f'Saldo Altos:')
print(saldo_alto)