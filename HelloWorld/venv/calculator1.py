def soma(x,y):
    z = x+y
    return z
def subt(x,y):
    z = x-y
    return z
def divy(x,y):
    z = x/y
    return z
def mult(x,y):
    z = x * y
    return z
state = True
lst = []
while state:
    op = input("Select your operation: ")
    print("Enter two numbers: ")
    for i in range(0,2):
        ele = int(input()
        lst.append(ele)
    if op == "+":
#      Obs; lst.insert(i,ele) nao funcionou por algum motivo.
        print(f"Sum = {soma(lst[0],lst[1])}")
        lst.clear()
    elif op == "-":
        print(f"Subtraction = {subt(lst[0,lst[1]])}")
        lst.clear()
    elif op == "/":
        print(f"Division = {divy(lst[0],lst[1])}")
        lst.clear()
    elif op == "*":
        print(f"Product = {mult(lst[0], lst[1])}")
        lst.clear()
    else:
        break

print("""
    E E E E E E E E E E E E
    E E E E E E E E E E E E
    E E E E E E E E E E E E
"""*500)

