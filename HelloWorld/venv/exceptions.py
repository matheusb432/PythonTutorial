try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError: # Excecao que afirma que nenhum numero pode ser dividido por 0.
    print('Age cannot be 0.')
except ValueError: # Caso a exceção ValueError for encontrada, o programa nao crashara e executara o codigo abaixo.
    print('Invalid value')
# Esse codigo pode lidar com 2 excecoes no codigo de try: