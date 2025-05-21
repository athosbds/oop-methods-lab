#Você recebeu duas listas com os nomes dos alunos que estiveram presentes em dois dias diferentes de aula. Use set para resolver as questões abaixo.

day1 = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduardo", "Fernanda"]
day2 = ["Beatriz", "Carlos", "Gabriel", "Helena", "Eduardo", "Isabela"]


present = set(day1).union(day2)
print(f'Presentes em um dos dois dias: {present}')
print(f'Presentes no primeiro dia: {day1}')

