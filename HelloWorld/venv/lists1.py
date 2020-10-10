numbers = [1,8,60,4,5,16]    # Lista ( mesmo que array ) de numeros
numbers_tuple = (1,8,60,4,5,16)
big_num = 0
for i in range(6):           # Funcao para achar o maior numero dessa lista
    if numbers[i] > big_num: # Se o numero do indice atual for maior que big_num ( que a principio, eh 0 ) , o big_num se torna esse numero
        big_num = numbers[i] # A condicao so se repete quando o numero do indice atual for maior que o maior numero ja percorrido na lista.
print(big_num)