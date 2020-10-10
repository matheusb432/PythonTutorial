class Point:  # 1. Convenção Pascal de nomenclatura, primeira letra maiuscula para classe. (Outro exemplo: EmailClient)  2. Sintaxe da classe => class NomeClasse:
    def move(self): # sintaxe do metodo
        print("move")

    def draw(self):
        print("draw")

point1 = Point() # Instanciando a classe num objeto point1, Sintaxe => objeto = Classe()
point1.x = 10  # Definindo dois atributos do objeto point1
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

