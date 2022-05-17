# 5.3. - Tuplas e Sequências

"""
Vimos que listas e strings têm muitas propriedades comuns, como operações de indexação e fatiamento. 

Eles são dois exemplos de tipos de dados de sequência (consulte Tipos de sequência — lista, tupla, intervalo). 

Como o Python é uma linguagem em evolução, outros tipos de dados de sequência podem ser adicionados.

Há também outro tipo de dados de sequência padrão: a tupla.

Uma tupla consiste em vários valores separados por vírgulas, e imutavel, por exemplo:
"""

tup = (12345, 54321, 'hello!')

print(tup)
# output: (12345, 54321, 'hello!')

# Mas eles podem conter objetos mutáveis:

tup = ([1, 2, 3], [3, 2, 1])

print(tup)
# output: ([1, 2, 3], [3, 2, 1])

"""
Não é possível atribuir aos itens individuais de uma tupla, no entanto, é possível criar tuplas que contenham objetos mutáveis, como listas.

Embora as tuplas possam parecer semelhantes às listas, elas são frequentemente usadas em diferentes situações e para diferentes propósitos. 

As tuplas são imutáveis e geralmente contêm uma sequência heterogênea de elementos que são acessados via descompactação ou indexação (ou mesmo por atributo no caso de tuplas nomeadas). 

As listas são mutáveis, e seus elementos são geralmente homogêneos e são acessados por iteração sobre a lista.

Um problema especial é a construção de tuplas contendo 0 ou 1 itens: a sintaxe tem algumas peculiaridades extras para acomodá-los. 

Tuplas vazias são construídas por um par de parênteses vazio; uma tupla com um item é construída seguindo um valor com uma vírgula (não é suficiente colocar um único valor entre parênteses). Por exemplo:
"""

vazio = ()
unico = 'hello',    # <-- note a virgula

print(len(vazio))
# output: 0

print(len(unico))
# output: 1

print(unico)
# output: ('hello',)
