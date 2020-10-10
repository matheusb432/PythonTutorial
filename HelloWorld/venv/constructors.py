class Point:  # 1. Convenção Pascal de nomenclatura, primeira letra maiuscula para classe. (Outro exemplo: EmailClient)  2. Sintaxe da classe => class NomeClasse:
    def __init__(self, x, y):  # 1. Um constructor em python, __init__ eh curto para initializer  2. Um constructor eh usado para construir/criar um objeto.
        self.x = x   # self eh uma referencia para o objeto atual,
        self.y = y   # no caso do objeto point, self definira o x e y do objeto point.

    def move(self): # sintaxe do metodo
        print("move")

    def draw(self):
        print("draw")

point = Point(10,20) # Passando dois parametros para a classe Point(), que serao definidos como atributos do objeto point
print(point.x)  # Chamando o atributo point.x do objeto point
# Exemplo simples:
class Person: # Classe Person
    def __init__(self, name): # Definindo o atributo name de um objeto instanciado nessa classe
        self.name = name # Definindo o atributo self.name com o argumento name que foi passado para esse metodo.
    def talk(self):
        print(f"{self.name} says Henlo.")

jamelao = Person("Jamelao Tobias") # Passando o atributo "Jamelao Tobias" como parametro da classe, este que se tornara atributo do objeto jamelao
jamelao.talk() # Executando o metodo talk() da classe Person com o objeto jamelao

meidao = Person("Meidao Meido") # Instanciando a classe novamente em outro objeto
meidao.talk()