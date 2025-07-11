import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
def increase(price):
    business = price * (10/100)
    total = price + business
    return total
def half(price):
    half_price = price / 2
    return half_price
def double(price):
    double_price = price * 2
    return double_price
def decrease(price):
    decrease_business = price * (10/100)
    total_dicrease = price - decrease_business
    return total_dicrease
def available_format(coin=0, matter=''):
    return f'{matter}{locale.currency(float(coin))}'