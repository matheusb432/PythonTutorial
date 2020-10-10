weight = int(input("How much do you weigh? "))
unit = input("(L)bs or (K)g? ")

if unit.upper() == 'L':         # Com o metodo .upper(), qualquer letra minuscula vira maiuscula, logo, a leitura deixa de ser case sensitive
    print(f'{weight * 0.45}Kg')
elif unit.upper() == 'K':       # Assim, o metodo upper() facilita a leitura de strings no caso de case sensitiviness.
    print(f'{weight / 0.45}Lbs')
else:
    print("Fuck off")