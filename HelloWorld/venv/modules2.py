import utils  # Nota: import utils executa todo o codigo de utils.py
from utils import define_list


list_modules = define_list(10)  # Chamando define_list diretamente com from utils import define_list
object_max = utils.find_max(list_modules)  # Chamando find_max com o objeto object_max, note que precisei especificar utils.find_max ja que nao importei a funcao diretamente.
print(f"Max = {object_max}")