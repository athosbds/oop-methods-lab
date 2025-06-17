# Filtrar códigos que começam com vogal, têm número ímpar e múltiplo de 3 ou 5
codes = ["A13", "B92", "C07", "D44", "E38", "F91", "G60", "H25", "I99", "J31"]
codes_filters = [
    code for code in codes 
    if code[0] in 'AEIOU'
    and int(code[1:]) % 2 == 1
    and (int(code[1:]) % 3 == 0 or (int(code[1:]) % 5 == 0))
]
print(codes_filters)