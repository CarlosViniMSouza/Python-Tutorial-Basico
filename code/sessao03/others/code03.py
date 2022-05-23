# LINK: https://www.w3schools.com/python/python_modules.asp

from modulo import pessoa02
import platform as pf
import modulo as md

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

md.saudacao("Carlos")
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


varNome = md.pessoa01["nome"]

print(f"\nNome em pessoa01: {varNome}")
# output: Nome em pessoa01: Carlos


"""
- Nomeando um Módulo:

  Você pode nomear o arquivo do módulo como quiser, mas deve ter a extensão de arquivo .py

- Renomear um módulo:
  
  Você pode criar um "apelido" ao importar um módulo, usando a palavra-chave 'as'

  Exemplo: Crie um apelido para modulo.py chamado 'md'
"""


# import modulo as md


"""
- Módulos integrados:

  Existem vários módulos integrados no Python, que você pode importar sempre que quiser.

  Exemplo: Importe e use o módulo da 'platform'
"""


var = pf.system()

print(f"\nNome do seu S.O. = {var}\n")
# output: Nome do seu S.O. = Windows


"""
- Usando a função dir():

  Existe uma função interna para listar todos os nomes de funções/variáveis em um módulo. A função dir():

  Exemplo: Liste todos os nomes definidos pertencentes ao módulo da plataforma
"""

var = dir(pf)

print(var)
"""
output:

[
  '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', '_os_release_candidates', '_os_release_line', '_os_release_unescape', '_parse_os_release', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_output', '_ver_stages', 'architecture', 'collections', 'freedesktop_os_release', 'functools', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver'
]
"""

"""
- Importar do módulo:

  Você pode optar por importar apenas partes de um módulo, usando a palavra-chave 'from'.

  Exemplo: Import o 'pessoa02' de modulo.py
"""

# from modulo import pessoa02  <- novamente, o corretor atrapalhando ...

print(f"\nMeu pais = " + pessoa02["pais"])
# output: Meu pais = Uruguai
