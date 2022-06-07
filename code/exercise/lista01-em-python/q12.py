"""
12. Faça um algoritmo que o usuário informe o raio de um círculo e mostre como resultado o perímetro e a área do círculo. Sabe-se que o perímetro é 2*π*raio e a área é π*raio2
"""

# 1° - declare as variaveis que precisamos (raio e valor do pi):
raio = float(input("Digite o valor do raio: "))

pi = 3.14

# 2° - calcule o que foi pedido(perímetro e área do círculo) -> lembre-se das formulas

perimetro = 2 * pi * raio

# <- dica: quando tiver que fazer radiciação/potenciação, coloque a expressão entre () para deixar o codigo mais 'entendivel' pros outros e para si!
area = pi * (raio**2)

# 3° - dar as respostas que o problema pede:

print("O valor do perimetro eh:", perimetro)

print("O valor da area eh:", area)
