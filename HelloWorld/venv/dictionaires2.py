number_decodificator = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4": "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
phone = input("Phone: ")
output = ""
for i in phone:
    output += number_decodificator.get(i, "!") + " "  # O indice ira percorrer cada letra da string phone.
print(output)                                         # + " " da um espaco entre cada palavra, output+= armazena a frase toda em uma so variavel.


#listt = []
#number = input("Number> ")
#n = len(number)
#print(n)
#int(number)
#for i in range(0,n):
#    x = int(input())
#    listt.append(x)
#    print(number_decodificator.get(listt[i]))
