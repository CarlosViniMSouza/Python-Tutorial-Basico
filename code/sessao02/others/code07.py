# 8.3 - Tratamento de Exceções

"""
Resumo brevedos "comandos"W:

  1. O bloco try permite testar um bloco de código quanto a erros.

  2. O bloco except permite que você lide com o erro.

  3. O bloco else permite executar código quando não há erro.

  4. O bloco finally permite que você execute código, independentemente do resultado dos blocos try e except.

- Manipulação de exceção:

  Quando ocorre um erro, ou exceção como chamamos, o Python normalmente irá parar e gerar uma mensagem de erro.

  Essas exceções podem ser tratadas usando a instrução try. 

  Exemplo: O bloco try irá gerar uma exceção, pois x não está definido:
"""


try:
    print(x)
except:
    print("Uma exceção ocorreu!")
# output: Uma exceção ocorreu!


"""
Como o bloco try gera um erro, o bloco except será executado.

Sem o bloco try, o programa irá travar e gerar um erro!

- Muitas exceções:

  Você pode definir quantos blocos de exceção quiser, por exemplo. se você quiser executar um bloco de código especial para um tipo especial de erro:

  Exemplo: Imprima uma mensagem se o bloco try gerar um 'NameError' e outra para outros erros.
"""


try:
    print(x)
except NameError:
    print("Variavel x não está definida")
except:
    print("Alguma coisa está errada")
# output: Variavel x não está definida


"""
- Else:

  Você pode usar a palavra-chave else para definir um bloco de código a ser executado se nenhum erro for gerado:

  Exemplo: No exemplo abaixo, o bloco try não gera nenhum erro.
"""


try:
    print("Ola Mundo")
except:
    print("Alguma coisa está errada")
else:
    print("Nada está errado")
"""
output:

Ola Mundo
Nada está errado
"""


"""
- Finally:

  O bloco finally, se especificado, será executado independentemente de o bloco try gerar um erro ou não.
"""


try:
    print("Oi")
except:
    print("Erro encontrado")
finally:
    print("Fim do caso de teste!")
"""
output:

Oi
Fim do caso de teste!
"""


"""
Isso pode ser útil para fechar objetos e limpar recursos:

Exemplo: Tente abrir e gravar em um arquivo que não seja gravável.
"""


try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Algo deu errado ao escrever no arquivo")
    finally:
        f.close()
except:
    print("Algo deu errado ao abrir o arquivo")


"""
(se o arquivo não existir) -> output: Algo deu errado ao abrir o arquivo

(por algum motivo, ele não produz o erro de 'Algo deu errado ao escrever no arquivo')

OBS.: O programa pode continuar, sem deixar o objeto de arquivo aberto.
"""

"""
- Criar uma exceção:

  Como desenvolvedor Python, você pode optar por lançar uma exceção se ocorrer uma condição.

  Para lançar (ou aumentar) uma exceção, use a palavra-chave raise.

  Exemplo: Gere um erro e pare o programa se x for menor que 0.
"""

x = -4

try:
    if x < 0:
        raise Exception("Numeros inferiores a 0 não são aceitos")
except:
    print("Tudo certo!")
# output: Tudo certo!


# Isso é, não poderemos exibir a menasagem de "Numeros inferiores a 0 não são aceitos"

"""
A palavra-chave raise é usada para gerar uma exceção.

Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.

Exemplo: Gere um TypeError se x não for um inteiro.
"""


x = "its String"

try:
    if (type(x) != int):
        raise TypeError("Apenas numeros inteiros sao aceitos")
except:
    print("Tudo certo!")
# output: Tudo certo!
