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


"""
- A função range():

  Para percorrer um conjunto de código um determinado número de vezes, podemos usar a função range(),
  A função range() retorna uma sequência de números, começando em 0 por padrão e incrementa em 1 (por padrão) e termina em um número especificado.

  Exemplo: Usando a função range()
"""

for i in range(6):
    print("O dobro de", i, "eh:", i*2)
"""
output:

O dobro de 0 eh: 0
O dobro de 1 eh: 2
O dobro de 2 eh: 4
O dobro de 3 eh: 6
O dobro de 4 eh: 8
O dobro de 5 eh: 10
"""

# NOTA: Observe que range(6) não são os valores de 0 a 6, mas os valores de 0 a 5.

"""
A função range() tem como padrão 0 como valor inicial, porém é possível especificar o valor inicial adicionando um parâmetro: range(2, 6), que significa valores de 2 a 6 (mas não incluindo 6):

Exemplo: Usando o parâmetro inicial
"""


for i in range(2, 6):
    print("O dobro de", i, "eh:", i*2)
"""
output:

O dobro de 2 eh: 4
O dobro de 3 eh: 6
O dobro de 4 eh: 8
O dobro de 5 eh: 10
"""


"""
A função range() padroniza para incrementar a sequência em 1, porém é possível especificar o valor do incremento adicionando um terceiro parâmetro: range(2, 30, 3):

Exemplo: Incremente a sequência com 3 (o padrão é 1)
"""


for i in range(2, 10, 2):
    print("O dobro de", i, "eh:", i*2)
"""
output:

O dobro de 2 eh: 4
O dobro de 4 eh: 8
O dobro de 6 eh: 12
O dobro de 8 eh: 16
"""


"""
- Else em for() Loop

  A palavra-chave else em um loop for especifica um bloco de código a ser executado quando o loop for concluído:

  Exemplo: Imprima todos os números de 0 a 5 e imprima uma mensagem quando o loop terminar
"""

for i in range(6):
    print("Numero:", i)
else:
    print("acabou!")
"""
output:

Numero: 0
Numero: 1
Numero: 2
Numero: 3
Numero: 4
Numero: 5
acabou!
"""


"""
NOTA: O bloco 'else' NÃO será executado se o loop 'for' interrompido por uma instrução break.

Exemplo: Interrompa o loop quando x for igual a 4 e veja o que acontece com o bloco else
"""


for x in range(6):
    print(x)
    if x == 4:
        break
else:
    print("acabou dnv!")
"""
output:

0
1
2
3
4
"""


"""
- Loops aninhados:

  Um loop aninhado é um loop dentro de um loop.

  O "loop interno" será executado uma vez para cada iteração do "loop externo":

  Exemplo: Imprima cada adjetivo para cada fruta
"""


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
"""
output:

red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""


"""
- A declaração de passagem(pass):

  loops for não podem ser vazios, mas se por algum motivo você tiver um loop for sem conteúdo, coloque a instrução pass para evitar erros.

  Exemplo:
"""

for i in range(5):
    pass


"""
É isso rapaziada, esse provavelmente será o último script que vou inserir nesse projeto.

Uma boa prova a todos!

dia: 31/05/2022
"""
