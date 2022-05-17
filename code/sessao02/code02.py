# 5.1. - Métodos em Listas

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

"""
Agora, vamos para os 3 métodos de remover.

OBS.: cuidado usar o metodo '.clear()' -> uma vez executado, seus dados serão apagados completamente (e nem adianta fazer Ctrl + Z pq eles não irão retornar!)
"""

# 1 - list.remove(x) -> esse eh facil de decorar! Remove o 1° item da lista cujo valor é igual a x. Mas para verem isso de fato, adicionarei o elemento "batata" no fim da lista:

# com isso, teremos os mesmos elementos, só que "batata" está em outra posição da lista_de_compras
lista_de_compras.append("batata")

lista_de_compras.remove("batata")

print(lista_de_compras)
# output: ['arroz', 'feijão', 'tomate', 'alface', 'frango', 'temperos', 'conservas', 'maionese', 'batata']

# 2 - list.pop(i) -> Remove o elemento na posição especificada na lista. Se nenhum índice for especificado, '.pop()' remove o último item da lista.

lista_de_compras.pop(3)  # remove 'alface'

print(lista_de_compras)

lista_de_compras.pop()  # remove 'batata'

print(lista_de_compras)

# 3 - list.clear() -> como disse anteriormente, apaga todas as informações contidas na lista:

lista_de_compras.clear()

print(lista_de_compras)
# output: []

# dados a serem usados no método de ordenação: ['arroz', 'feijão', 'tomate', 'alface', 'frango', 'temperos', 'conservas', 'maionese', 'batata']

"""
Por fim, o último método a ser explicado, o de ordenação: list.sort(*, key=None, reverse=False)

1 - Funcionalidade: Retorna uma nova lista ordenada dos itens em iterável.

2 - Saiba que: Possui 2 argumentos opcionais que devem ser especificados como argumentos de palavra-chave:

    2.1 - 'key' especifica uma função de um argumento que é usado para extrair uma chave de comparação de cada elemento em iterável (por exemplo, key=str.lower). O valor padrão é Nenhum (compare os elementos diretamente).
    
    2.2 - 'reverse' é um valor booleano. Se definido como True, os elementos da lista serão classificados inversamente.

Agora, vamos fazer alguns testes:
"""

lista_de_compras = ['arroz', 'feijão', 'tomate', 'alface',
                    'frango', 'temperos', 'conservas',
                    'maionese', 'batata']

lista_de_compras.sort()
print(lista_de_compras)
# output: ['alface', 'arroz', 'batata', 'conservas', 'feijão', 'frango', 'maionese', 'temperos', 'tomate']

lista_de_compras.sort(key=None, reverse=True)
print(lista_de_compras)
# output: ['tomate', 'temperos', 'maionese', 'frango', 'feijão', 'conservas', 'batata', 'arroz', 'alface']

lista_de_compras.sort(key=None, reverse=False)
print(lista_de_compras)
# output: ['alface', 'arroz', 'batata', 'conservas', 'feijão', 'frango', 'maionese', 'temperos', 'tomate']
# igual ao primeiro teste, se reparar!
