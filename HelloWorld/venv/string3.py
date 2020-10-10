course = 'Python for Beginners'
print(len(course)) # Ve o tamanho da string
print(course.upper()) # Metodo para transformar a string em letras maiusculas, nao modifica a string mas sim cria uma nova string.
print(course.lower()) # Metodo para transformar a string em letras minusculas.
print(course.find('P')) # Metodo que procura onde comeca a posicao da letra P, eh case sensitivive.
print(course.replace('Beginners', 'Starters')) # Metodo para substituir uma(s) letra(s) na string
print('Python' in course) # Expressao booleana para ver se a Python esta na string course.