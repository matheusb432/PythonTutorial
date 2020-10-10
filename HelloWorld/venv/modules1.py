import converters  # Importando converters.py para modules.py como se fosse um objeto
from converters import kg_to_lbs  # Importando a funcao diretamente de converters.py

# Modulos sao formas mais faceis de deixar o codigo limpo, sem repetir nada.

print(converters.kg_to_lbs(90))  # Chamando como se fosse um objeto, com a sintaxe objeto.metodo(parametros)
print(kg_to_lbs(100))  # Ao inves de precisar chamar o objeto, basta apenas chamar a funcao com essa forma.
