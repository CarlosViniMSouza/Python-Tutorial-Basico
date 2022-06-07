"""
16. Escreva um algoritmo que apresente como resultado o valor em graus Fahrenheit de uma temperatura dada em graus Celsius. Para isso, leia o valor da temperatura em graus Celsius e aplique a seguinte fórmula para o cálculo da temperatura em Fahrenheit: F = (9 * C)/5 + 32.
"""

# 1° - variaveis:

temperatura = float(input("Digite o valor da temperatura: "))

# 2° - processos(solução):

# f = temperatura em Fahrenheit:
f = (9 * temperatura)/5 + 32

# 3° - respostas:

print("O valor da temperatura em Fahrenheit eh:", f)
