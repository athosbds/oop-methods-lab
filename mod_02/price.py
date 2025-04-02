def aumento(price: float, upper: int):
    total_upper = price * (upper/100)
    result = total_upper + price
    return result
def diminuir(price: float, lower: int):
    total_lower = price * (lower/100)
    result_lower = price - total_lower
    return result_lower
def resume(price: float, upper: int, lower: int):
    upper_price = aumento(price, upper)
    lower_price = diminuir(price, lower)
    print(f'\nPreço Analisado: {price} \nDobro do Preço: {price*2} \nMetade do preço: {price/2} \nPreço Aumentando {upper}%: {upper_price} \nPreço Diminuindo {lower}%: {lower_price}')