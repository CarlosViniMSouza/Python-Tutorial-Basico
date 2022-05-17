# 4.2 - Loops for()

"""
A instrução for() em Python difere um pouco do que você pode estar acostumado em C ou Pascal. 

A instrução for() do Python itera sobre os itens de qualquer sequência (uma lista ou uma string), na ordem em que aparecem na sequência. Por exemplo:
"""

bichos = ["cachorros", "passaros", "ouriços", "lontras", "gatos"]

"""
1 - Nossa variavel de iteração 'i' lerá cada string da lista.
2 - O método 'len()' retorna o tamanho de uma string.
"""

for i in bichos:
    print(i, "contem", len(i), "letras")

# 4.3 - A função range():

"""
Se você precisar iterar sobre uma sequência de números, a função interna range() é útil. 

Ela gera progressões aritméticas:
"""

for i in range(5):
    print(i)

"""
range(5) gera 5 valores, os índices legais para itens de uma sequência de comprimento 5. 

É possível deixar o intervalo começar em outro número, ou especificar um incremento diferente (mesmo negativo; às vezes isso é chamado de 'passo'(step)). Exemplo:

NOTA: O que fizemos abaixo, foi gerar uma lista que executa o range(), que produzirá seu conteúdo:
"""

# aqui, ele irá imprimir os numeros desde 5 até 9 (excluindo o numero dado como limite (10) !!)
print(list(range(5, 10)))
# output: [5, 6, 7, 8, 9]

# aqui, ele "pula" de 3 em 3 numeros ate o limite do range()
print(list(range(1, 12, 3)))
# output: [1, 4, 7, 10]

# e o exemplo de que é possivel usar negativos no range()
print(list(range(-10, -50, -15)))
# output: [-10, -25, -40]


# Para iterar sobre os índices de uma sequência, você pode combinar 'range()' e 'len()' da seguinte forma:

for i in range(len(bichos)):
    print(i, bichos[i])

"""
Dizemos que 'range()' é iterável, ou seja, adequado para funções que esperam itens consecutivos até que o limite seja alcançado(ou se esgote quase que por completo). 

Veja um exemplo de função que recebe um iterável sum():
"""

print(sum(range(0, 20, 3)))
# output: 63
# |-> (0 + 3 + 6 + 9 + 12 + 15 + 18) = 63


# LINK para mais estudos sobre Controle de Fluxo: https://docs.python.org/3/tutorial/controlflow.html
