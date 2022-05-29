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

"""
for() -> para(cont = 0; cont <= 10; cont++) # <- NAO LEMBRO!
"""

for var in bichos:
    print(var, "contem", len(var), "letras")
"""
output:

cachorros contem 9 letras
passaros contem 8 letras
ouriços contem 7 letras
lontras contem 7 letras
gatos contem 5 letras
"""


# 4.3 - A função range():

"""
Se você precisar iterar sobre uma sequência de números, a função interna range() é útil. 

Ela gera progressões aritméticas: a(n), a(n+1), a(n+2), ... (termo de progressao 'p')

a(n+1) = a(n) + p
a(n+2) = a(n+1) + p
"""

for i in range(5):
    # i == 5 -> break (no Portugol eh para)
    print(i)
"""
output:

0
1
2
3
4
"""

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

# bichos = ["cachorros", "passaros", "ouriços", "lontras", "gatos"]

for i in range(len(bichos)):
    print(i, bichos[i])
"""
output:

0 cachorros
1 passaros
2 ouriços
3 lontras
4 gatos
"""

"""
Dizemos que 'range()' é iterável, ou seja, adequado para funções que esperam itens consecutivos até que o limite seja alcançado(ou se esgote quase que por completo). 

Veja um exemplo de função que recebe um iterável sum(): (sum -> somatorio)
"""

print(sum(range(0, 20, 3)))
# output: 63
# |-> (0 + 3 + 6 + 9 + 12 + 15 + 18) = 63


# LINK para mais estudos sobre Controle de Fluxo: https://docs.python.org/3/tutorial/controlflow.html
