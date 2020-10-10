numbers = [2,2,2,2,5]
for x_count in numbers:              # Fazendo um for com dois indices, ou coordenadas.
    output = ''                      # Output zera a quantia de x
    for count in range(x_count):     # Percorre x_count, no caso, sera executado 5,2,5,2 e 2 vezes.
        output += 'x'                # adiciona um x para cada loop
    print(output)                    # printa no fim de cada loop x_count para formar o L