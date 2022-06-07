"""
14. Faça um algoritmo que leia um capital C, uma taxa de juros mensal fixa J e um período de aplicação em meses M. Calcule e mostre o montante F arrecadado no final do período: F = C*(1+J/100)*M.
"""

# 1° - variaveis que precisamos:

capital = float(input("Qual o valor do capital?: "))

# j = Taxa de Juros Mensal Fixa
j = float(input("Qual a Taxa de Juros Mensal?: "))

# m = Periodo de Aplicação em Meses
m = float(input("Quantos meses?: "))

# 2° - pega a formula e joga numa variavel (resumidamente ...):

# f = montante
f = capital * (1 + j/100) * m

# 3° - resposta:

print("O montante acumulado foi:", f)
