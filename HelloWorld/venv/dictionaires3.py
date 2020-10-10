message = input(">")
words = message.split(' ')  # Usando o metodo split(), que, quando detectar um espaco [' '], ira separar a string entre varias outras strings/palavras que serao armazenadas numa lista.
# A variavel words eh uma lista de strings.
emojis = {
    ":)": "(❁´◡`❁)",
    ":(": "(T_T)",
    ":/": "(⊙ˍ⊙)"
}
output = ""
for word in words:
    output += emojis.get(word, word) + ' '  # Caso o dicionario ter a traducao da palavra, imprimira essa traducao, se nao, apenas imprimira a palavra nao traduzida.
#    if word == ":)" or word == ":(" or word == ":/":
#        print(f"{emojis.get(word) + ' '}")
#    else:
#        print(i)
print(output)
