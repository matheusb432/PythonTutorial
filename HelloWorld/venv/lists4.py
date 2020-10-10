# Codigo que remove numeros duplicados em uma funcao
numbers = [1,2,3,3,4,4,5,6,7,7,8,8,10,26,34,26]
print(numbers)
for number in numbers:
#    duplicate = numbers.count(number)
    if numbers.count(number) > 1:    # Se a quantidade de instancias for maior que 1 ( duplicate ) , remover o numero em questao.
        numbers.remove(number)
print(numbers)
