# input()

print("oi")

# variaveis

"""
inteiro n1, n2

escreva("digite valor 01: ")
leia(n1)

escreva("digite valor 02: ")
leia(n2)

-10, 0, 5, ... (1.5 != inteiro, mas com ponto flutuante(float))
"""

variavel = 1

print(type(variavel))
# <class 'int'>

var = input("Pfv, digite um numero: ")

print("seu numero eh: ", var)

print(type(var))
# <class 'str'>

# qualquer info passada no input(), será visto como string! (string -> "cadeia de caracteres")

# para transformar 'str' em 'int', faça o seguinte:

var = int(input("Pfv, digite um numero: "))  # int(), float(), ...

print("seu numero eh: ", var)

print(type(var))
# <class 'int'>

var = float(input("Pfv, digite um numero: "))

print("seu numero eh: ", var)

print(type(var))
# <class 'float'>
