numbers = [5,2,1,7,4]
numbers.append(10)        # Adiciona um numero a lista
numbers.insert(2, 4)      # Insere um numero n em um um indice i (i,n)
# numbers.remove(5)         Remove um numero x
# numbers.clear()           Remove todos os numeros
# numbers.pop()             Remove o ultimo numero da lista
print(numbers)
print(numbers.index(7))   # Pega o indice do numero x
print(numbers.count(4))   # Pega a quantia de vezes que x eh instanciado
numbers.sort()            # Ordena a lista em ordem crescente
numbers2 = numbers.copy() # Copia a lista em questao
numbers.reverse()         # Reverte a ordem dos numeros, quando combinado com o metodo sort() ele deixa a lista em ordem decrescente.
print(numbers2)           # Ordem crescente
print(numbers)            # Ordem decrescente