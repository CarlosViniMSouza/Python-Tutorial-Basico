# LINK: https://www.w3schools.com/python/python_classes.asp

"""
- Classes/objetos Python:

  Python é uma linguagem de programação orientada a objetos.

  Quase tudo em Python é um objeto, com suas propriedades e métodos.

  Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.
"""

"""
- Criar uma classe:

  Para criar uma classe, use a palavra-chave 'class'.

  Exemplo: Crie uma classe chamada "MinhaClasse", com uma propriedade chamada "x"
"""




from asyncio.windows_events import NULL
class MinhaClasse:
    x = 10


"""
- Criar objeto
  
  Agora podemos usar a classe chamada MyClass para criar objetos:

  Exemplo: Crie um objeto chamado "p1" e imprima o valor de "x"
"""

p1 = MinhaClasse()

print(f"\nMeu numero eh: {p1.x}")
# output: Meu numero eh: 10


"""
- A função __init__():

  Os exemplos acima são classes e objetos em sua forma mais simples e não são realmente úteis em aplicações da vida real.

  Para entender o significado das classes, temos que entender a função __init__() embutida.

  Todas as classes possuem uma função chamada __init__(), que sempre é executada quando a classe está sendo iniciada.

  Use a função __init__() para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado:
"""


class Pessoa:
    def __init__(self, nome, idade, genero) -> None:
        self.nome = nome
        self.idade = idade
        self.genero = genero

        print(
            f"\nMinha ficha: \nNome: {nome}, \nIdade: {idade}, \nGenero: {genero}"
        )  # essa linha eu adicionei de propósito!!


p1 = Pessoa("Carlos", 21, 'M')  # essa linha exibira as infos
"""
output:

Minha ficha: 
Nome: Carlos, 
Idade: 21, 
Genero: M
"""


# NOTA: A função __init__() é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.


"""
- Métodos de objeto:

  Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.

  Vamos criar um método na classe Person!

  Exemplo: Insira uma função que imprima uma saudação e execute-a no objeto p1
"""


class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def hello(self):
        print(f"\nOla! Meu nome eh {self.nome}")


p1 = Pessoa("Vinicius", 21, 'M')

p1.hello()
# output: Ola! Meu nome eh Vinicius

# NOTA: O parâmetro 'self' é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe.


"""
- O parâmetro self:

  O parâmetro 'self' é uma referência à instância atual da classe e é usado para acessar variáveis que pertencem à classe.

  Ele não precisa ser nomeado 'self', você pode chamá-lo como quiser, mas deve ser o primeiro parâmetro de qualquer função na classe:

  Exemplo: Use as palavras 'meuObjeto' e 'abc' em vez de self
"""


class Pessoa:
    def __init__(meuObjeto, nome, idade):
        meuObjeto.nome = nome
        meuObjeto.idade = idade

    def hello(abc):
        print(f"\nOi! Minha idade eh {abc.idade}")


p1 = Pessoa("Carlos", 21)

p1.hello()
# output: Oi! Minha idade eh 21


"""
- Modificar propriedades do objeto:

  Você pode modificar propriedades em objetos como este:

  Exemplo: Defina a idade de p1 para 40
"""

p1.idade = 22

p1.hello()
# output: Oi! Minha idade eh 22


"""
- Excluir propriedades do objeto:
  
  Você pode excluir propriedades em objetos usando a palavra-chave 'del':

  Exemplo: Exclua a propriedade 'idade' do objeto p1
"""

del p1.idade

"""
- Excluir objetos:

  Você pode excluir objetos usando a palavra-chave 'del':

  Exemplo: Exclua o objeto p1
"""

del p1

"""
- A declaração de passagem:

  As definições de classe não podem estar vazias, mas se por algum motivo você tiver uma definição de classe sem conteúdo, coloque a instrução 'pass' para evitar erros. Exemplo:
"""


class Pessoa:
    # nao acontece nada
    pass
