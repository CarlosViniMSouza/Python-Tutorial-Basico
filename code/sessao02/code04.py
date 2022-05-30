# 5.3. - Tuplas e Sequências

"""
Vimos que listas e strings têm muitas propriedades comuns, como operações de indexação e fatiamento (e a concatenação). Eles são dois exemplos de tipos de dados de sequência.

Como o Python é uma linguagem em evolução, outros tipos de dados de sequência podem ser adicionados. Há também outro tipo de dado de sequência padrão: a Tupla. Veja uns exemplos:
"""

tup = (12345, 54321, 'hello!')

print(tup)
# output: (12345, 54321, 'hello!')

# Podem conter objetos mutáveis:

tup = ([1, 2, 3], [3, 2, 1])

print(tup)
# output: ([1, 2, 3], [3, 2, 1])

"""
Embora as tuplas possam parecer semelhantes às listas, elas são frequentemente usadas em diferentes situações e para diferentes propósitos. 

As tuplas são imutáveis e geralmente contêm uma sequência heterogênea de elementos que são acessados via descompactação ou indexação (ou mesmo por atributo no caso de tuplas nomeadas).

Um problema especial é a construção de tuplas contendo 0 ou 1 itens: a sintaxe tem algumas peculiaridades extras para acomodá-los. 

Tuplas vazias são construídas por um par de parênteses vazio; uma tupla com um item é construída seguindo um valor com uma vírgula (não é suficiente colocar um único valor entre parênteses). Por exemplo:
"""

vazio = ()
unico = 'hello',    # <-- note a virgula

print(len(vazio))
# output: 0

print(len(unico))
# output: 1

print(vazio)
# output: ()

print(unico)
# output: ('hello',)
