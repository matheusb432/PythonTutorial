def greet_user(first_name, last_name):   # Funcoes em Python  Sintaxe => { def function_name(parameters): }
    print(f'Hello {first_name + " " + last_name}')
    print('Welcome aboard')


def calc_cost(total,shipping,discount):
    cost = total + shipping
    adjust = cost * discount
    true_cost = cost - adjust
    print(true_cost)


print("Start")
name = input("What's your first name? ")
name2 = input("What's your last name? ")
greet_user(name, last_name=name2)        # Chamando a funcao
    # Ordem = (argumentos posicionais, argumentos keyword)
calc_cost(total=50, shipping=5, discount=0.1)        # Keyword arguments, serve para deixar o codigo mais legivel.
print("Finish")