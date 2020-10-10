class Mammal:  # Superclasse Mammal
    def walk(self):
        print("walk")


class Dog(Mammal): # Subclasse Dog, que herda tudo de Mammal
    def bork(self):
        print("bork")


class Cat(Mammal): # Subclasse Cat, que herda tudo de Mammal
    pass # pass serve para definir uma classe vazia sem o Python se emputecer contigo.

sig = Dog()
fig = Cat()
sig.walk()
sig.bork()
fig.walk()
