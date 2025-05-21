#Você recebeu duas listas com os nomes dos alunos que estiveram presentes em dois dias diferentes de aula. Use set para resolver as questões abaixo.

day1 = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduardo", "Fernanda"]
day2 = ["Beatriz", "Carlos", "Gabriel", "Helena", "Eduardo", "Isabela"]


present = set(day1).union(day2)
print(f'\nPresentes em um dos dois dias: {present}')
print(f'\nPresentes no primeiro dia: {day1}')

both_days = set(day1).intersection(day2)
print(f'\nPresentes nos dois dias: {both_days}')

total = len(present)
print(f'\nAlunos diferentes: {total}')