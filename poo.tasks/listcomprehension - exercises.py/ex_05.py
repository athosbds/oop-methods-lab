#Transforme a lista ['Ana', 'Bruno', 'Carlos'] em uma lista só com as iniciais dos nomes usando list comprehension.

names = ['Ana', 'Bruno', 'Carlos'] 
new_name = [name[0] for name in names]
print(new_name)
