# LINK: https://www.w3schools.com/python/python_inheritance.asp

"""
- Herança Python:

  A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.

  A 'classe pai' é a classe que está sendo herdada, também chamada de "classe base".

  A 'classe filha' é a classe que herda de outra classe, também chamada de "classe derivada".
"""

"""
- Criar uma classe pai:

  Qualquer classe pode ser uma classe pai, então a sintaxe é a mesma da criação de qualquer outra classe:

  Exemplo: Crie uma classe chamada Pessoa, com as propriedades 'nome' e 'sobrenome' e um método 'exibirNome':
"""


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibirNome(self):
        print(f"\nSeu nome eh {self.nome} {self.sobrenome}")


pessoa = Pessoa("Carlos", "Souza")

pessoa.exibirNome()
# output: Seu nome eh Carlos Souza


"""
- Criar uma classe filha:

  Para criar uma classe que herde a funcionalidade de outra classe, envie a classe pai como parâmetro ao criar a classe filha:

  Exemplo: Crie uma classe chamada 'Estudante', que herdará as propriedades e métodos da classe Pessoa.
"""


class Estudante(Pessoa):
    pass

# NOTA: Use a palavra-chave 'pass' quando não quiser adicionar outras propriedades ou métodos à classe.


"""
Agora a classe 'Estudante' tem as mesmas propriedades e métodos que a classe Pessoa.

Exemplo: Use a classe 'Estudante' para criar um objeto e execute o método "exibirNome".
"""

estudante = Estudante("Vinicius", "Souza")

estudante.exibirNome()
# output: Seu nome eh Vinicius Souza


"""
- Adicione a função __init__():

  Até agora criamos uma classe filha que herda as propriedades e métodos de seu pai.

  Queremos adicionar a função '__init__()' à classe filha (em vez da palavra-chave 'pass').

  NOTA: A função __init__() é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.

  Exemplo: adicione a função __init__() a classe Estudante.
"""

"""
NOTA01: Quando você adiciona a função __init__(), a 'classe filha' não herdará mais a função __init__() da 'classe pai'.

NOTA02: A função __init__() do filho substitui a herança da função __init__() do pai.
"""


class Estudante(Pessoa):
    def __init__(self, nome, sobrenome):
        """
        Para manter a herança da função __init__() do pai,
        adicione uma chamada à função __init__() do pai:
        """
        Pessoa.__init__(self, nome, sobrenome)


"""
Agora adicionamos com sucesso a função __init__() e mantivemos a herança da classe pai, e estamos prontos para adicionar funcionalidade na função __init__().
"""

"""
- Use a função super():

Python também tem uma função super() que fará com que a classe filha herde todos os métodos e propriedades de seu pai. Exemplo:
"""


class Estudante(Pessoa):
    def __init__(self, nome, sobrenome):
        """
        Ao utilizar 'super()', a classe herdará 
        os métodos e propriedades da outra.
        """
        super().__init__(nome, sobrenome)


"""
- Adicionar Propriedades:

  Adiciona uma propriedade chamada 'anoGraduacao' na classe Estudante!
"""


class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, ano):
        super().__init__(nome, sobrenome)
        self.anoGraduacao = ano

        print(f"\nDiscente: {nome} {sobrenome}")
        print(f"\nGraducao: {ano}")
        # as 2 ultimas linhas eu adicionei!


estudante = Estudante("Carlos", "Souza", 2024)
"""
output:

Discente: Carlos Souza

Graducao: 2024
"""


"""
- Adicionar metodos:

  Adicione um metodo chamado 'BoasVindas' na classe Estudante:
"""


class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, ano):
        super().__init__(nome, sobrenome)
        self.anoGraduacao = ano

    def BoasVindas(self):
        print(
            f"\nBem-Vindo(a) {self.nome} {self.sobrenome} a turma graduanda {self.anoGraduacao}")


estudante = Estudante("Carlos", "Sousa", 2023)

estudante.BoasVindas()
# output: Bem-Vindo(a) Carlos Sousa a turma graduanda 2023


"""
Se você adicionar um método na classe filha com o mesmo nome de uma função na classe pai, a herança do método pai será substituída.

Agora, so falta o code03.py -> Modulos Python
"""
