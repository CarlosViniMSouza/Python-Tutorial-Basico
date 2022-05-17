# 3.1.2 - Strings

"""
Além de números, o Python também pode manipular strings, que podem ser expressas de várias maneiras. 

Eles podem ser colocados entre aspas simples ('...') ou aspas duplas ("...") com o mesmo resultado. a cotnra-barra (\) pode ser usada para escapar de aspas:
"""

print('emails de spam')  # aspas simples
# output: emails de spam

print('doesn\'t')        # use \ para escapar das aspas simples...
# output: doesn't

print("doesn\'t")        # ... ou use aspas duplas
# output: doesn't

print('"Sim", eles disseram.')
# output: "Sim", eles disseram.

print("\"Sim\" eles disseram.")
# output: "Sim", eles disseram.

print('"Isn\'t,", they said.')
# output: "Isn't,", they said.

"""
No interpretador interativo, a string de saída é colocada entre aspas e os caracteres especiais são escapados com barras invertidas.

A função print() produz uma saída mais legível, omitindo as aspas e imprimindo caracteres de escape e especiais:
"""

frase = "Primeira linha\nSegunda linha"

print(frase)

"""
output:

Primeira linha
Segunda linha
"""

"""
Curiosidade: Se você não quiser que os caracteres precedidos por \ sejam interpretados como caracteres especiais, você pode usar strings brutas adicionando um 'r' antes da primeira aspa. Exemplo:
"""

print(r"Testando: \funcionou\reprovou\aprovado!")
# output: Testando: \funcionou\reprovou\aprovado!

"""
Faremos +2 operações: concatenando strings de 'forma direta' e 'forma indireta'
"""

# 1 - Forma direta (os espaços nas 2 últimas strings é para deixar algum espaçamento nas palavras):

print("Py" + "thon" + " eh" + " legal!!")
# output: Python eh legal!!

# 2 - Forma indireta (usando variaveis do tipo string):

nome = "Carlos"

print("Bem-Vindo " + nome)
