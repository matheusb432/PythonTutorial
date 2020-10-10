def define_list(size_of_list):
    list = []
    for i in range(size_of_list):
        element = int(input(f'Enter element {i} of the list: '))
        list.append(element)
    return list


def find_max(list):
    maximum = None
    for number in list:
        if maximum == None: # Obs; sso eh o mesmo que max = list[0] para a busca linear, so quis fazer uma zuada mesmo.
            maximum = number
        elif number > maximum:
            maximum = number
    return maximum  # Obs; max() eh um funcao embutida em Python, porem quando se redefine como variavel, ela deixa de ser funcao para o programa em questao.
                    # Entao renomeei a variavel para nao acontecer isso, pois nao eh recomendado.

#list = define_list(5)

#print(f'Max = {find_max(list)}')