"""
13. Faça um algoritmo para imprimir a área de um triângulo. Sabe-se que a área é (base*altura)/2.
"""

"""
Eu deveria ter explanado melhor na questão 12, mas farei aqui:

-> A solução de um problema pode ser tratada em 3 etapas:

1° - variaveis: Pensar em quantas/quais/como devem ser!
2° - solução: lógica/raciocinio que usará as variaveis para produzir uma resposta
3° - respostas: entregar o que foi requisitado/esperado (pode acontecer de vc ter que fazer essa etapa durante a 2°)

Bem, vamos lá:
"""

# 1° - as variaveis que precisamos(a questão nao informou, mas temos que pedir 2 informações: 'base' e 'altura'):

base = float(input("Digite o valor da base: "))

altura = float(input("Digite o valor da altura: "))

# 2° - a logica (aqui vamos pegar aquela formula da area, dada no enunciado):

area = (base*altura)/2

# 3° - respostas (dar o que o problema quer):

print("O valor da area eh:", area)
