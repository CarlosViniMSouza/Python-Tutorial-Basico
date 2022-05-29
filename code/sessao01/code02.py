# 3.1.2 - Strings

"""
Além de números, o Python também pode manipular strings, que podem ser expressas de várias maneiras. 

Eles podem ser colocados entre aspas simples ('...') ou aspas duplas ("...") com o mesmo resultado. a contra-barra (\) pode ser usada para escapar de aspas:
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

nome = "Ana"

print(f"Bem-Vindo {nome}")
# output: Bem-Vindo Carlos

"""
AGORA A COISA VAI FICAR UM POUCO CONFUSA, VÁ COM CALMA!!

Strings podem ser indexadas(subscritos); o primeiro caractere tem índice 0. Não há um tipo de caractere separado; um caractere é simplesmente uma string de tamanho um:
"""

palavra = "paralelepípedo"

# Indo da esquerda p/ direita:

print(palavra[0])
# output: p -> primeira letra

print(palavra[13])
# output: o -> ultima letra

# Os índices também podem ser números negativos, para começar a contar da direita: (<-)

print(palavra[-1])
# output: o -> ultima letra

print(palavra[-14])
# output: p -> primeira letra

"""
Além da indexação, o fatiamento também é suportado. 

Enquanto a indexação é usada para obter caracteres individuais, o fatiamento permite obter uma sub-string:
"""

# 1 - caracteres da posição 0 (incluída) a 4 (excluída):
print(palavra[0:4])
# output: para

# 2 - caractere do início até a posição 4 (excluída):
print(palavra[:4])
# output: para

# 3 - caracteres da posição 4 (incluída) até o final:
print(palavra[4:])
# output: lelepípedo

# 4 - caracteres do décimo elemento (incluído) até o final:
print(palavra[-4:])
# output: pedo

"""
Essa seria a forma como o Python particiona a string da variavel 'palavra':

   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   | p | a | r | a | l | e | l | e | p | í | p | e | d | o |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
  -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

A primeira linha de números fornece a posição dos índices 0 … 14 na string; a segunda linha fornece os índices negativos correspondentes.
"""

# LINKS UTEIS:

# 1 - Metodos de Strings: https://docs.python.org/3/library/stdtypes.html#string-methods
# 2 - Sintaxe de String de Formato: https://docs.python.org/3/library/string.html#formatstrings
