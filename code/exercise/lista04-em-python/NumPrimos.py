"""
Faça um programa que peça um número inteiro
e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

# aqui, ele vai exibir uma qtd de numero primos.
# nao eh o que a questao pede, mas ja eh um começo.
num = int(input("Digite um numero: "))

for i in range(1, num+1):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i)
