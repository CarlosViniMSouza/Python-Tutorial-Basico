# 9 - Classes

"""
As classes fornecem um meio de agrupar dados e funcionalidades. A criação de uma nova classe cria um novo tipo de 'objeto' (EXPLIQUE O QUE É OBJETO!), permitindo que novas 'instâncias' (EXPLIQUE O QUE É INSTÂNCIA!) desse tipo sejam feitas. 

Cada instância de classe pode ter atributos anexados a ela para manter seu estado. As instâncias de classe também podem ter métodos (definidos por sua classe) para modificar seu estado.

A forma mais simples de definição de classe:
"""


class Classnome:
    # statement-01
    # ...
    # statement-02
    pass


"""
Instruções de classe, assim como instruções de função, devem ser executadas antes de terem qualquer efeito.

Na prática, as instruções dentro de uma classe geralmente serão instruções de uma função, mas outras instruções são permitidas e, às vezes, úteis. (RESUMINDO: Operações feitas por uma classe, geralmente é obra de funções contidas nessa classe).

Agora, vejamos esse assunto mais a fundo!
"""

"""
- Objetos de classe:

Objetos de classe suportam dois tipos de operações: referências de atributo e instanciação.

As "referências de atributo" utilizam a sintaxe-padrão usada para todas as referências de atributo em Python: 'obj.nome'. 

Os nomes de atributos válidos são todos os nomes que estavam no campo da classe quando o 'objeto de classe' foi criado.

Então, confira um exemplo de classe:
"""


class MeuRegistro:
    rg = 123987  # <- Atributo válido da classe

    # Objeto da Classe: Função com uma finalidade
    def root(self):
        return "✌️ ~ Eai galerinha!"


"""
A instanciação de classe usa notação de função. Apenas finja que o objeto de classe é uma função sem parâmetros que retorna uma nova instância da classe. Por exemplo:
"""

var = MeuRegistro()

"""
☝️ Cria uma nova instância da classe e atribui esse objeto à variável local 'var'.

A 'operação de instanciação' ("chamar" um objeto de classe) cria um objeto vazio. 

Muitas classes criam objetos com instâncias personalizadas para um estado inicial específico.

EXTRA: Uma classe pode definir um método especial chamado '__init__()':
"""


class criarFuncaoComplexa:
    def __init__(self, realPart, imgPart):
        self.real = realPart
        self.imag = imgPart


var2 = criarFuncaoComplexa(2.0, -6.5)

print(f"funcao complexa: {var2.real} + ({var2.imag})*i")
# output: funcao complexa: 2.0 + (-6.5)*i

"""
- Objetos de instância:

Agora, o que podemos fazer com objetos de instância? A única operação compreendida por objetos de instância são referências de atributo. 

Existem 2 tipos de nomes de atributos válidos: atributos de dados e métodos.

    Sobre os Atributos de Dados:

    1 - Atributos de Dados correspondem a "variáveis de instância".

    2 - Os Atributos de Dados não precisam ser declarados; como variáveis locais, elas surgem quando são atribuídas pela primeira vez.

Por exemplo, se 'var' for a instância de 'MeuRegistro' criada acima, o seguinte trecho de código imprimirá o valor 16:
"""

var.counter = 1
while(var.counter < 10):
    var.counter = var.counter * 2

print(var.counter)
# output: 16

"""
O outro tipo de referência de atributo de instância é um método!

Um método é uma função que pertence a um objeto. Exemplo:
"""

# A função root() contida em MeuRegistro se tornou um método para 'var'
print(var.root())
# output: ✌️ ~ Eai galerinha!

"""
- Objetos de método:

Normalmente, um método é chamado logo após ser vinculado. Exemplo: print(var.root())

No exemplo acima, isso retornará a string 'Eai galerinha! ✌️'. 

No entanto, não é necessário chamar um método imediatamente: 'var.root' é um objeto de método e pode ser armazenado e chamado posteriormente.
"""

varRoot = var.root
cont = 0

# o 'cont' tem como papel encerrar o loop.
while(cont < 4):
    # simplificando, o conteúdo no método 'var.root' está guardado na variavel 'varRoot'
    print(varRoot())
    cont += 1


"""
- Variáveis de classe e instância:

De um modo geral, as "variáveis de instância" são para dados exclusivos de cada instância e as "variáveis de classe" são para atributos e métodos compartilhados por todas as instâncias da classe:
"""


class Doguinho:
    especie = 'canino'         # variavel de classe compartilhada para todas as instâncias

    def __init__(self, nome):
        # variável de instância única para cada instância (nesse caso, é 'dog01' e 'dog02')
        self.nome = nome


dog01 = Doguinho('Fido')
dog02 = Doguinho('Buddy')

print(dog01.especie)    # compartilhado por todos os cães
# output: 'canino'

print(dog02.especie)    # compartilhado por todos os cães
# output: 'canino'

print(dog01.nome)       # exclusivo para variavel 'dog01'
# output: 'Fido'

print(dog02.nome)       # exclusivo para variavel 'dog02'
# output: 'Buddy'


"""
Bem, deixarei a questão do estudo de Classes até aqui.

Esse é um conceito de muita importância no Python! Pois as classes são peça-chave para Orientação a Objetos (POO) e Modularização (conceito fundamental para arquitetura de Microsserviços).

(OBS.: Esse assuntos serão vistos no futuro, e muito provavelmente, abordados em outras LPs)

LINK: https://docs.python.org/3/tutorial/classes.html

Agora só falta 2 tópicos: Herança(um pouco puxadinho) e Módulos(algo básico, mas que deve ser explicado)
"""
