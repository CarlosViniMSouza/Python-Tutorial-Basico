# 6 - Módulos

"""
Um módulo é um arquivo que contém definições e declarações python. O nome do arquivo é o nome do módulo com o apêndice sufixo. Dentro de um módulo, o nome do módulo (como uma string) está disponível como o valor da variável global. 

Por exemplo, crie um arquivo chamado 'fibo.py' com os seguinte conteúdo:
"""

from modules import fibo  # <- isso foi o corretor do VS Code que deixou!!


def fib(n):    # escreva a série de Fibonacci até n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    # print()  # eu nao sei o porque desse print() vazio!


def fib2(n):   # retorna a série de Fibonacci até n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# agora vamos testar a importação do fibo.py

print(fibo.fib(100))
# output:
# 0 1 1 2 3 5 8 13 21 34 55 89
# None

print(fibo.fib2(100))
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
