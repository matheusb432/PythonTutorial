is_hot = False
is_cold = False

if is_hot:          # Prestar atencao no espacamento (indentation) do if statement, em Python nao ha {} aparentemente.
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:       # Caso a condicao if for false, elif (else if) sera verificada.
    print("It's a cold day")
    print("Wear warm clothes")
else:               # Caso ambas as condicoes forem falsas, else sera executada.
    print("What a lovely day")
# Sintaxe: ( if x:    elif x:   else: )