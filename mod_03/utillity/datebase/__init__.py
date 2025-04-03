def readvalue(message):
    confirm = False
    while not confirm:
        deploy = str(input(message)).replace(',', '.').strip()
        if deploy.isalpha() or deploy == '':
            print(f'Erro! INVÁLIDO!')
        else:
            confirm = True
    return float(deploy)