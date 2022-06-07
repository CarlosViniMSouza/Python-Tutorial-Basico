"""
30. Escreva um algoritmo que leia três números inteiros (A, B, C) e calcule a seguinte expressão:

D = (R + S)/2, sabendo que:

R = (A + B)^2
S = (B + C)^2
"""

# 1° - variaveis:

A = int(input("Digite o valor de A: "))

B = int(input("Digite o valor de B: "))

C = int(input("Digite o valor de C: "))

# 2° - processo:

R = (A + B) * (A + B)  # ou (A + B) ** 2

S = (B + C) * (B + C)  # ou (B + C) ** 2

D = (R + S)/2

# 3° - respostas:

print("O valor de D eh:", D)
