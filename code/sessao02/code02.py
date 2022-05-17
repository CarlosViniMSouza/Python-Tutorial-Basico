# 5.1. - More on Lists

"""
Como disse anteriormente, existem diversos métodos para se trabalhar com Listas.

E abordarei apenas aqueles que acredito serem mais relevantes (e não há nada de difícil em entender um método - pode ser chato para relembrar, mas com muita prática, você aprende!)

Começando pelos 2 métodos de adição
"""

lista_de_compras = ["arroz", "feijão", "batata",
                    "tomate", "alface", "frango",
                    "conservas"]

# sera necessario?: qtd = [3, 3, 8, 4, 10, 2, 3]

# 1 - list.append(x) -> adiciona um novo elemento no fim da lista:

lista_de_compras.append("maionese")

print(lista_de_compras)
# output: ['arroz', 'feijão', 'batata', 'tomate', 'alface', 'frango', 'conservas', 'maionese']

# 2 - list.insert(i, x) -> insire um elemento em uma determinada posição. Exemplo: adicione 'temperos' antes de 'conservas'

lista_de_compras.insert(-2, "temperos")

print(lista_de_compras)
# output: ['arroz', 'feijão', 'batata', 'tomate', 'alface', 'frango', 'temperos', 'conservas', 'maionese']
