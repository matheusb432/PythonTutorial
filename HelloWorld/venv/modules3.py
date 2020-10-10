import random  # Importando o módulo embutido random do Python 3


class Dice:
    def __init__(self, lst):
        self.lst = lst
        for i in range(0, 2):
            element = random.randint(1, 6)
            self.lst.append(element)

    def dice_roll(self):
        self.dice_tuple = (lst[0], lst[1])
        return self.dice_tuple
    # print(f'({self.dice_tuple})')
    # return (first, second) ja retorna um tuple implicito


lst = []
listrand = Dice(lst)  # Objeto listrand que recebe parametro lst
result = listrand.dice_roll
print(f'{result}')

members = ['John', 'Mary', 'Bob', 'Matheus']
leader = random.choice(members)  # choice() aleatoriamente  escolhe um elemento da lista.
print(leader)
# for i in range(3):
#    print(random.random())  # Chamando o módulo random como se fosse um objeto
#    print(random.randint(10, 20))  # random() gera um decimal entre 0 e 1, randint(x,y) gera um inteiro entre 10 e 20
