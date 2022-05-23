# LINK: https://www.w3schools.com/python/python_modules.asp

import modulo

"""
Modulos Python

- O que é um Módulo?

  Considere um módulo como sendo o mesmo que uma biblioteca de código.

  Um arquivo contendo um conjunto de funções que você deseja incluir em seu aplicativo.

- Criar um módulo:

  Para criar um módulo basta salvar o código desejado em um arquivo com a extensão de arquivo .py:

  Exemplo: Crie e Salve o código abaixo em um arquivo chamado 'modulo.py':
"""


def saudacao(nome):
    print(f"\nOla {nome}! Prazer em conhecer você!")


"""
- Usar um módulo:

  Agora podemos usar o módulo que acabamos de criar, usando a instrução import:

  Exemplo: Importe o módulo chamado mymodule e chame a função de saudação:
"""

# import modulo <- o corretor do VS Code jogou o 'import modulo' p/ linha 20
# e eu joguei para a linha 3!! 🤣

modulo.saudacao("Carlos")
# output: Ola Carlos! Prazer em conhecer você!

# NOTA: Ao usar uma função de um módulo, use a sintaxe: module_name.function_name.

"""
- Variáveis no Módulo:

  O módulo pode conter funções, como já descrito, mas também variáveis de todos os tipos (arrays, dicionários, objetos etc):

  Exemplo: Salve este código no arquivo modulo.py
"""

pessoa01 = {
    "nome": "Carlos",
    "idade": 22,
    "pais": "Brasil"
}


varNome = modulo.pessoa01["nome"]

print(f"\nNome em pessoa01: {varNome}")
# output: Nome em pessoa01: Carlos
