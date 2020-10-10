matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]      # Matriz bi-dimensional em Python
print(matriz[0][1]) # Matriz [Linha][Coluna]
for linha in matriz:
    for coluna in linha:
        print(coluna)

numbers = (1,2,3)   # numbers = (n1,n2,n3...) eh um Tuple, basicamente uma lista que nao pode ser modificada.
print(numbers[0])