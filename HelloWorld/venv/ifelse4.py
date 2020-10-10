temperature = int(input("What's the temperature in Celsius? "))

if temperature >= 30:        # A logica condicional em Python segue a mesma sintaxe que em C, ou seja, ==, >, <, >=, <=, != e if(x)/if x: caso x for True
    print("It's a hot day")
elif temperature <= 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")