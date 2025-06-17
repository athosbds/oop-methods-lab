# Filtrar códigos cuja letra inicial não seja X, Y, Z, número maior que 20 e não múltiplo de 3
codigos = ["X14", "Y29", "Z50", "W13", "V40", "U23", "T36", "S45", "R60", "Q37"]
filter = [
    code for code in codigos 
    if code[0] != 'XYZ'
    and int(code[1:]) % 3 != 0
    and int(code[1:]) > 20
]

print(filter)