# 5.5 - Dicionários

"""
Outro tipo de dados útil incorporado ao Python é o dicionário. Dicionários às vezes são encontrados em outras línguas como "memórias associativas" ou "matrizes associativas". 

Ao contrário das sequências, que são indexadas por um intervalo de números, os dicionários são indexados por chaves, que podem ser de qualquer tipo; strings e números sempre podem ser chaves. 

Você não pode usar listas como chaves, pois as listas podem ser modificadas no local usando atribuições de índice, atribuições de fatia ou métodos como '.append()' e '.extend()'

É melhor pensar em um dicionário como um conjunto de 'chaves: pares' de valores, com o requisito de que as chaves sejam únicas (dentro de um dicionário). Um par de chaves cria um dicionário vazio: {}. 

Colocar uma lista separada por vírgulas de pares 'chave:valor' dentro das chaves adiciona pares 'chave:valor' inicial ao dicionário; esta é também a forma como os dicionários são escritos na saída.

As principais operações em um dicionário são armazenar um valor com alguma chave e extrair o valor fornecido pela chave.

Executar 'list(d)' em um dicionário retorna uma lista de todas as chaves usadas no dicionário, na ordem de inserção (se você quiser classificá-lo, basta usar 'sorted(d)'. Para verificar se uma única chave está no dicionário, use a palavra-chave 'in'.

Aqui está um pequeno exemplo usando um dicionário:
"""

# temos o nosso 1° dicionario
tel = {'jack': 4098, 'sape': 4139}

# agora, vamos adicionar um par 'chave:valor'
tel['guido'] = 4127


print(tel)
# output: {'jack': 4098, 'sape': 4139, 'guido': 4127}


# para exibir o valor de uma chave, basta chamar-mos tal chave:
print(tel['jack'])
# output: 4098


# deletando um par 'chave:valor' do dicionario
del tel['sape']


# adicionando outro para substituir o anterior:
tel['irv'] = 4127


print(tel)
# output: {'jack': 4098, 'guido': 4127, 'irv': 4127}


# exibir todas as chaves em uma lista
print(list(tel))
# output: ['jack', 'guido', 'irv']


# ordenar exibição das chaves:
print(sorted(tel))
# output: ['guido', 'irv', 'jack']


# Checando se existe tal cheva em nosso dicionario:

print('guido' in tel)
# output: True

print('jack' not in tel)
# output: False


# O construtor 'dict()' constrói dicionários diretamente de sequências de pares chave-valor:

dicionario = dict(
    [('aluno01', 2020004567),
     ('aluno02', 2021002654),
     ('aluno03', 2022001998)]
)

print(dicionario)
# output: {'aluno01': 2020004567, 'aluno02': 2021002654, 'aluno03': 2022001998}

# Uma outra forma de criarmos dicionarios (quando o componenete 'chave' for string):
dicionario = dict(
    aluno01=2020004567,
    aluno02=2021002654,
    aluno03=2022001998
)

print(dicionario)
# output: {'aluno01': 2020004567, 'aluno02': 2021002654, 'aluno03': 2022001998}


"""
Se não estou enganado, existem métodos para dicionários que nos permitem fazer operações como:

- inclusão
- exclusão
- pesquisa
- confirmação
"""
