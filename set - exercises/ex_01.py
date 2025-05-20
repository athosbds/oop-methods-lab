#Você está ajudando um professor a controlar a presença dos alunos na aula. Ele tem duas listas: A lista de alunos matriculados A lista de alunos que estiveram presentes hoje

matriculados = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]
presentes = ["Ana", "Carlos", "Eduardo", "Carlos", "Ana"]

set_matriculados = set(matriculados)
set_presentes = set(presentes)
faltaram = set_matriculados - set_presentes

quantidade_faltas = len(faltaram)
quantidade_presente = len(presentes)

todos = set_matriculados.union(set_presentes)
print(f'Alunos que faltaram: {faltaram}\nQuantidade presentes: {quantidade_presente}\nQuantidade De Faltantes: {quantidade_faltas}\nTodos: {todos}')