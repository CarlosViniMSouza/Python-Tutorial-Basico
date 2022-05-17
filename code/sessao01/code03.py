# 4.1 - Condicionais if(), elif() e else

# Talvez o tipo de instrução mais conhecido seja a instrução if. Por exemplo:

x = int(input("Digite um numero inteiro: "))

if x < 0:
    print('Negativo')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Um')
else:
    print('Maior que 1')

"""
Pode haver zero ou mais partes 'elif', e a parte 'else' é opcional. 

A palavra-chave 'elif' é a abreviação de 'else if' e é útil para evitar recuo excessivo. 

Uma sequência if … elif … elif … é um substituto para as instruções 'switch case' encontradas em outras linguagens.

NOTA: em versões python 3.10.x podemos usar o 'match case'. 

Para obter mais detalhes, consulte a doc do match case: https://docs.python.org/3/tutorial/controlflow.html#match-statements.
"""
