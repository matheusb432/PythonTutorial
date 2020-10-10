# Exemplo 1
year = input('What year you were born in? ')
print(type(year))             # Funcao para informar qual o tipo da variavel
age = 2020 - int(year)        # Usando int() para converter a string year em um integer year, o mesmo pode ser feito com float() e bool() ou ate str()
print(type(age))
print('You are ' + str(age) + ' years old')
# Exemplo 2
weight_lbs = input('How much do you weight in lbs? ')
weight_kg = float(weight_lbs) / 2.205
print('You weigh ' + str(weight_kg) + ' in kg')