# 8.3. Tratamento de exceções

"""
É possível escrever programas que tratam de exceções selecionadas. Veja o exemplo a seguir, que solicita a entrada do usuário até que um inteiro válido seja inserido, mas permite que o usuário interrompa o programa.

Usando Ctrl+C ou o que o sistema operacional suporta; observe que um usuário-interrupção gerada é sinalizada levantando a exceção KeyboardInterrupt.
"""

import sys
while True:
    try:
        x = int(input("Por favor, digite um numero inteiro: "))
        break  # quando enviamos um numero inteiro, o break eh ativado!
    except ValueError:
        print("Isso nao eh um numero inteiro! Tente novamente")

"""
A instrução 'try' funciona da seguinte maneira.

° Primeiro, a cláusula try (a(s) instrução(ões) entre as palavras-chave try e except) é executada.

° Se nenhuma exceção ocorrer, a cláusula except será ignorada e a execução da instrução try será concluída.

° Se ocorrer uma exceção durante a execução da cláusula try, o restante da cláusula será ignorado. 
  Então, se seu tipo corresponder à exceção nomeada após a palavra-chave except, a cláusula except será executada e a execução continuará após o bloco try/except.

° Se ocorrer uma exceção que não corresponda à exceção nomeada na cláusula except, ela será passada para instruções try externas; 
  Se nenhum manipulador for encontrado, é uma exceção sem tratamento e a execução é interrompida com uma mensagem conforme mostrado acima.
"""

"""
Uma classe em uma cláusula 'except' é compatível com uma exceção se for a mesma classe ou uma classe base dela (mas não o contrário - uma cláusula except listando uma classe derivada não é compatível com uma classe base). 

Por exemplo, o código a seguir imprimirá B, C, D nessa ordem:
"""


class TeamB(Exception):
    pass


class TeamC(TeamB):
    pass


class TeamD(TeamC):
    pass


for cls in [TeamB, TeamC, TeamD]:
    try:
        raise cls()
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
Observe que se as cláusulas except fossem invertidas (com except B primeiro), teriamos impresso B, B, B — a primeira cláusula except correspondente é acionada.

Todas as exceções herdam de 'BaseException' e, portanto, podem ser usadas para servir como curinga. Use isso com extrema cautela, pois é fácil mascarar um erro de programação real dessa maneira! Ele também pode ser usado para imprimir uma mensagem de erro e, em seguida, aumentar novamente a exceção. Exemplo:
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

Logo abaixo, o link com toda a documentação Python para tratativas

LINK: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions
"""
