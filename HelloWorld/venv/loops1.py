import random # Biblioteca de numeros aleatorios
number = random.randint(0,10) # o metodo randint() gera um inteiro entre x e y aleatorio.
print(number)
guess_count = 0  # Obs; shift+F6 facilita renomear todas as instancias de uma variavel para algo mais descritivo ( no caso tornei i em guess_count )
guess_limit = 3
while guess_count < guess_limit: # A sintaxe eh while condition:
    guess = int(input('Guess any integer between 0 and 10: '))
    if guess == number:
        print('You won!')
        break   # Igual ao C, encerra o loop.
    elif guess != number:
        guess_count += 1
        if guess_count == guess_limit:
             print(f'The number was {number}, you failed!')