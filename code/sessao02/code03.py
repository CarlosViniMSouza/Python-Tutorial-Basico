# 5.1.4 - Compreensão de lista aninhada (lista 2D)

"""
A expressão inicial em uma compreensão de lista pode ser qualquer expressão arbitrária, incluindo outra compreensão de lista.

Considere o seguinte exemplo de uma matriz 3x4 implementada como uma lista de 3 listas de comprimento 4:
"""

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

"""
A compreensão de lista irá transpor linhas e colunas. E podemos imprimir a matriz transposta usando 'for()':

Processa cada elemento da matrix, retornando 4 listas de 3 elementos cada. O for() dividirá os elementos por meio do indice.
"""

mat = []

for i in range(4):
    mat.append([linha[i] for linha in matrix])

print(mat)
# output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


"""
Podemos imprimir nossa matriz usando a função zip().

Para melhorar o compactamento, colocamos um '*' antes da variavel:
"""

print(list(zip(*mat)))
# output: [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]

"""
Enfim, listas bidimensionais podem ser bem trabalhosas, e não há muito conteúdo na documentação referente a esse tópico.

Agora, vamos conferir outros tipos de dados(tuplas e dicionarios)
"""
