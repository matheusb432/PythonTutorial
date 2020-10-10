credit = int(input('Do you have good credit? Type 1 for yes and 0 for no ')) # OBSERVACAO: sem especificar que o int() do input, a variavel sera lida como uma string.
price = int(input('What is the price of the house that you want to buy? '))

if credit == 1:
    down_payment = price / 10
    print(f"Down payment: R${down_payment}")
elif credit == 0:
    down_payment = price / 5
    print(f"Down payment: R${down_payment}")

