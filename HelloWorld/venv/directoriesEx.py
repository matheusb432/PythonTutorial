from pathlib import Path  # Obs; from {module} import {class}

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin
# Relative path
path = Path()  # Instancia a classe Path no objeto path
#  mkdir() cria directory, rmdir() remove
# '*' significa tudo, procura no directory
# *.py procura todos os arquivos.py no directory
# Com esse for eh possivel percorrer to-do elemento do metodo e printar na tela.
for file in path.glob('*'):
    print(file)

