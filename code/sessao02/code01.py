# 3.1.3 - Listas

"""
Python conhece vários tipos de dados compostos, usados para agrupar outros valores. 

A mais versátil é a lista, que pode ser escrita como uma lista de valores separados por vírgulas (itens), e entre colchetes. As listas podem conter itens de tipos diferentes, mas GERALMENTE todos os itens têm o mesmo tipo. Exemplo:
"""

nums = [1, 4, 9, 16, 25]

print(nums)
# output: [1, 4, 9, 16, 25]

variados = [1, 2.5, 'b', "Ola", False]

print(variados)
# output: [1, 2.5, 'b', "Ola", False]

"""
Assim como as strings (e todos os outros tipos de sequência integrados), as listas podem ser indexadas e divididas(particionadas):

(Vejamos o "mesmos processos" que fizemos com strings):
"""

print(nums[1])
# output: 4

print(nums[-2])
# output: 16

print(nums[:3])
# output: [1, 4, 9]

print(variados[3:])
# output: ['Ola', False]

print(variados[2:4])
# output: ['b', 'Ola']


# As listas também suportam concatenação(junção):

print(nums + [36, 49, 64, 81, 100])
# output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# No entanto, diferente de strings, listas são mutaveis(podemos substituir qualquer 1 de seus elementos). Exemplo:

# substituindo o booleano 'False' pelo 'True':
variados[-1] = True

print(variados)
# output: [1, 2.5, 'b', "Ola", True]

"""
Agora, vem a parte de métodos!

No entanto, existem diversos metodos para listas (dos mais variados tipos, tamanhos e formatos). Por isso abordarei os seguintes métodos:

1 - Adicionar elemento (list.append(x))
2 - Adicionar elemento em uma posição específica (list.insert(i, x))

3 - Remover elemento (list.remove(x))
4 - Remover elemento em uma posição específica (list.pop([i]))
5 - Remover todos os elementos (list.clear())

6 - Ordenar elementos (list.sort(*, key=None, reverse=False))

E sugiro que vejam os demais métodos em: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""
