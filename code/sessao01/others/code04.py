# LINK: https://www.w3schools.com/python/python_for_loops.asp

"""
- Python para loops:

  Um loop 'for()' é usado para iterar sobre uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string).

  Isso é menos parecido com a palavra-chave 'for' em outras linguagens de programação e funciona mais como um método iterador, conforme encontrado em outras linguagens de Programação Orientadas a Objetos.

  Com o loop 'for' podemos executar um conjunto de instruções, uma vez para cada item de uma lista, tupla, conjunto etc.

  NOTA: iteração == repetição

  Exemplo: Imprima cada fruta em uma lista de frutas
"""


fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
"""
output: 

apple
banana
cherry
"""


"""
NOTA: O loop 'for' não requer que uma variável de indexação seja definida antecipadamente.

- Fazendo um loop em uma string:

  Mesmo as strings são objetos iteráveis, elas contêm uma sequência de caracteres:

  Exemplo: Percorra as letras da palavra "banana"
"""


for x in "banana":
    print(x)
"""
output:

b
a
n
a
n
a
"""


"""
- A declaração de pausa(break):

  Com a instrução break podemos parar o loop antes que ele tenha percorrido todos os itens:

  Exemplo: Saia do loop quando x for "strewberry"
"""


fruits = ["apple", "banana", "cherry", "strewberry", "grape"]

for x in fruits:
    if x == "strewberry":
        break
    print(x)
"""
output: 

apple
banana
cherry
"""


"""
- A declaração continua(continue):

  Com a instrução continue podemos parar a iteração atual do loop e continuar com a próxima:

  Exemplo: Não imprima "cherry"
"""


for x in fruits:
    if x == "cherry":
        continue
    print(x)
"""
output:

apple
banana
strewberry
grape
"""
