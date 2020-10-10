prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total = 0
total2=0
i=0
for item in range(0,10):  # Sintaxe: for [variavel] in range(x,y,z): [duracao do loop de x a y, z eh quantos passos a funcao da a cada loop]
    total += prices[item]
    if item == 9:
        print(total)
for price in prices:  # Tambem da pra percorrer um array especifico utilizando uma variavel
    total2 += price
    print(price)
    if price == 100:
        print(total2)