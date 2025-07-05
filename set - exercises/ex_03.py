futebol = {"Ana", "Lucas", "João", "Thiago", "Julia"}
xadrez = {"Ana", "Lucas"}
teatro = {"João", "Julia", "André"}

frequent_students = (futebol & xadrez)|(futebol & teatro) | (xadrez & teatro)
noun_chess = set(futebol | teatro) - set(xadrez)
everyone = set(futebol | teatro | xadrez)
only_teather = teatro - set(futebol | xadrez) 

print(f""""
    Alunos que participam mais de 1 atividade: {frequent_students}
    Alunos que não participaram de Xadrez: {noun_chess}
    Todos os Participantes: {everyone}
    Somente Teatro: {only_teather}""")