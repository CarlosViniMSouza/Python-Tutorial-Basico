"""
17. Faça um algoritmo que leia o valor do raio de uma esfera e calcule seu volume que é dado pela fórmula V = (4 * π * raio3) / 3.
"""

"""
Gente, eu vou ficar repetindo esse processo até vcs seus cerébros absorverem essa informação:
"""

# 1° - variaveis:
raio = float(input("Digite o valor do raio: "))

pi = 3.14

# 2° - processos:

# v = volume da esfera
# raio ao cubo(raio ** 3) = raio * raio * raio
# (fiz desse jeito pois vc pode acabar nao lembrando do '**')
v = (4 * pi * (raio * raio * raio))/3

# 3° - resposta:
print("O volume da esfera eh:", v)
