customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}                                     # Definindo um dicionario com chaves, bem parecido com o struct do C
print(customer["name"])               # Acessando a key "name" do dicionario customer.
print(customer.get("age"))            # Com o metodo get(), o codigo nao da erro caso a key nao existir, e apenas apresenta None no output.
customer["birthdate"] = "Set 4 2000"  # Tambem da pra adicionar outro valor key para o dicionario de maneira externa.
print(customer.get("birthdate"))