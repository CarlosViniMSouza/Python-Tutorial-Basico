# RECOMENDO USAR O OTHERS/CODE07.PY para melhor compreensão deste tema em específico

# 8.3. Tratamento de exceções

"""
Explicando brevemente os conceitos de 'try' e 'except':

1 - O bloco 'try' permite testar um bloco de código quanto a erros.

2 - O bloco 'except' permite que você lide com o erro.

É possível escrever programas que tratam de exceções selecionadas. Veja o exemplo a seguir, que solicita a entrada do usuário até que um inteiro válido seja inserido, mas permite que o usuário interrompa o programa.
"""

while True:
    try:
        x = int(input("Por favor, digite um numero inteiro: "))
        break  # quando enviamos um numero inteiro, o break eh ativado!
    except ValueError:
        print("Isso nao eh um numero inteiro! Tente novamente")

"""
A instrução 'try' funciona da seguinte maneira.

    1. A cláusula 'try' é executada;

    2. Se nenhuma exceção ocorrer, a cláusula 'except' será ignorada e a execução da instrução 'try' será concluída; (Caso 1)

    3. Se ocorrer uma exceção, o restante da cláusula 'try' será ignorado; (Caso 2)

    4. Se ocorrer uma exceção que não corresponda à exceção nomeada em 'except', vamos ao 'try' externo; (Caso 3)

Uma classe com uma cláusula 'except' é compatível com uma exceção se for a mesma classe ou uma classe base dela (Isso pode parecer meio confuso em uma primeira leitura). Por exemplo, o código a seguir imprimirá B, C, D nessa ordem:
"""


class TeamB(Exception):
    pass


class TeamC(TeamB):
    pass


class TeamD(TeamC):
    pass


for cls in [TeamB, TeamC, TeamD]:
    try:
        raise cls()  # <- 'raise' é uma peculiaridade a ser estudada
    except TeamD:
        print("D")
    except TeamC:
        print("C")
    except TeamB:
        print("B")
"""
output:

B
C
D
"""

"""
Observe que se as cláusulas 'except' fossem invertidas (com 'except' B primeiro), teriamos impresso B, B, B — A primeira cláusula 'except' correspondente é acionada.

Todas as exceções herdam de 'BaseException' e, portanto, podem ser usadas para servir como curinga. Use isso com extrema cautela, pois é fácil mascarar um erro de programação real dessa maneira! Exemplo:
"""

try:
    arquivo = open('code\sessao02\myfile.txt')
    string = arquivo.readline()
    inteiro = int(string.strip())
except OSError as err:
    print("erro do S.O. : {0}".format(err))

except ValueError:
    print("Nao foi possivel converter os dados em um numero inteiro.")

except BaseException as err:
    print(f"Inesperado {err=}, {type(err)=}")
    raise

"""
Ele gera mensagens de erro caso:

1 - se o arquivo não existir
2 - se o arquivo existe, mas estiver vazio
3 - se o conteudo do arquivo nao for um numero inteiro
4 - se o argumento passado em 'open()' não for o caminho que leva ao arquivo
"""

"""
Gente, tem muito conteúdo para estudar sobre Tratamento de Erros!

Por isso, só vou dar uma pincelada nesse assunto (pois é um tópico muito extenso, cansativo, e que poderá gerar muitas dúvidas durante os primeiros estudos).

Mas é algo importante, pois ajuda na detecção de erros e prevenção de futuros problemas na aplicação (principalmente quando se trata de manipular dados ou arquivos).

Logo abaixo, o link com toda a documentação Python para 'try ... except'

LINK: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions
"""
