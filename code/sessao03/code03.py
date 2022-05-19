# 6 - Módulos

"""
Se você sair do interpretador Python e inseri-lo novamente, as definições que você fez (funções e variáveis) são perdidas. Portanto, se você quiser escrever um programa um pouco mais longo, é melhor usar um editor de texto para preparar a entrada para o interpretador e executá-lo com esse arquivo como entrada.

Isso é conhecido como criar um script. À medida que seu programa fica mais longo, você pode querer dividi-lo em vários arquivos para facilitar a manutenção. Você também pode querer usar uma função útil que você escreveu em vários programas sem copiar sua definição em cada programa.

Para suportar isso, o Python tem uma maneira de colocar definições em um arquivo e usá-las em um script ou em uma instância interativa do interpretador.

Tal arquivo é chamado de módulo; definições a partir de um módulo podem ser importadas em outros módulos ou no módulo principal (a coleção de variáveis a que você tem acesso em um script executado no nível superior e no modo calculadora).

Um módulo é um arquivo que contém definições e declarações python. O nome do arquivo é o nome do módulo com o apêndice sufixo. Dentro de um módulo, o nome do módulo (como uma string) está disponível como o valor da variável global. 

Por exemplo, use seu editor de texto favorito para criar um arquivo chamado no diretório atual com os seguintes conteúdos: fibo.py
"""

"""fibo.py
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
"""


# agora vamos testar a importação do fibo.py

from modules import fibo
print(fibo.fib(1000))
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# None

print(fibo.fib2(100))
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
