# 3.1.1 Numbers

"""
O interpretador funciona como uma calculadora simples: você pode digitar uma expressão nele e ele escreverá o valor.

A sintaxe da expressão é direta: os operadores +, -, * e / funcionam como na maioria das outras linguagens; parênteses podem ser usados para agrupamento. Por exemplo:
"""

print(2 + 2)
# output: 4

print(50 - 5*6)
# output: 20

print((50 - 5*6) / 4)
# output: 5.0

# divisão sempre retorna um número de "ponto flutuante"(decimal)
print(8/5)
# output: 1.6

"""
Os números inteiros (por exemplo, 2, 4, 20) são do tipo int.
Aqueles com parte fracionária (por exemplo, 5.0, 1.6) são do tipo float.

Veremos mais sobre tipos numéricos posteriormente no tutorial.

A divisão (/) sempre retorna um float. 
Para fazer a divisão do numero e obter um resultado inteiro você pode usar o operador //;

Para calcular o restante você usar %:
"""

# 1 - divisão clássica:
print(17 / 3)
#output: 5.666666666666667

# 2 - divisão descartando a parte fracionaria/decimal:
print(17 // 3)
#output: 5

# 3 - o operador % retorna o resta da divisão:
print(17 % 3)
#output: 2

# 4 - quociente * divisor + resto:
print(5 * 3 + 2)
#output: 17

# Com Python, é possível usar o operador ** para calcular potências:

print(5 ** 2)
# output: 25

print(4 ** 4)
# output: 256

# O sinal de igual (=) é usado para atribuir um valor a uma variável:

largura = 20
altura = 5 * 9
print(largura * altura)
# output: 900

"""
Além de int e float, o Python suporta outros tipos de números, como Decimal e Fraction. 
Python também tem suporte embutido para números complexos e usa o sufixo j ou J para indicar a parte imaginária. Exemplo:
"""

numComplexo = 4 + 6j

print(type(numComplexo))
# output: <class 'complex'>
