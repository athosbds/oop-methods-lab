from utillity import coin
from utillity.datebase import readvalue
commom = 'Digite um preço:R$ '
value = readvalue(commom)
coin.resume(value, 20, 10)
