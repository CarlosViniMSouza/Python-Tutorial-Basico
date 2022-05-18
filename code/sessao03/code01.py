# 9 - Classes

"""
As classes fornecem um meio de agrupar dados e funcionalidades. A criação de uma nova classe cria um novo tipo de objeto, permitindo que novas instâncias desse tipo sejam feitas. 

Cada instância de classe pode ter atributos anexados a ela para manter seu estado. As instâncias de classe também podem ter métodos (definidos por sua classe) para modificar seu estado.

As classes introduzem um pouco de nova sintaxe, três novos tipos de objetos e algumas novas semânticas.

A forma mais simples de definição de classe:
"""


from tabnanny import check


class ClassName:
    # statement-01
    # ...
    # statement-02
    pass


"""
Instruções de classe, assim como instruções de função (instruções def) devem ser executadas antes de terem qualquer efeito.

Na prática, as instruções dentro de uma classe geralmente serão instruções de uma função, mas outras instruções são permitidas e, às vezes, úteis. 

As instruções da função dentro de uma classe normalmente têm uma forma peculiar de lista de argumentos, ditada pelas convenções de chamada para 'métodos'.
"""

"""
- Objetos de classe:

Objetos de classe suportam dois tipos de operações: referências de atributo e instanciação.

As referências de atributo usam a sintaxe padrão usada para todas as referências de atributo em Python: obj.name. 

Os nomes de atributos válidos são todos os nomes que estavam no namespace da classe quando o objeto de classe foi criado. 

Então, a classe ficaria assim:
"""


class MeuRegistro:
    rg = 123987

    def root(self):
        return "Eai galerinha! ✌️"


"""
A instanciação de classe usa notação de função. Apenas finja que o objeto de classe é uma função sem parâmetros que retorna uma nova instância da classe. Por exemplo (assumindo a classe acima):
"""

var = MeuRegistro()

"""
☝️ Cria uma nova instância da classe e atribui esse objeto à variável local 'var'.

A operação de instanciação ("chamar" um objeto de classe) cria um objeto vazio. 

Muitas classes gostam de criar objetos com instâncias personalizadas para um estado inicial específico. 

Portanto, uma classe pode definir um método especial chamado __init__(), assim:
"""


class FunComplex:
    def __init__(self, realPart, imgPart):
        self.real = realPart
        self.imag = imgPart


var2 = FunComplex(2.0, -6.5)

print(f"funcao complexa: {var2.real} + ({var2.imag})i")

"""
- Objetos de instância:

Agora, o que podemos fazer com objetos de instância? As únicas operações compreendidas por objetos de instância são referências de atributo. 

Existem 2 tipos de nomes de atributos válidos: atributos de dados e métodos.

Sobre os Atributos de Dados:

1 - atributos de dados correspondem a "variáveis de instância".

2 - Os atributos de dados não precisam ser declarados; como variáveis locais, elas surgem quando são atribuídas pela primeira vez.

Por exemplo, se 'var' for a instância de MeuRegistro criada acima, o seguinte trecho de código imprimirá o valor 16, sem deixar rastro:
"""

var.counter = 1
while var.counter < 10:
    var.counter = var.counter * 2
print(var.counter)
del var.counter

"""
O outro tipo de referência de atributo de instância é um método. Um método é uma função que pertence a um objeto. Exemplo:
"""

var.root()  # <- a função root() contida em MeuRegistro se tornou um método para 'var'

"""
Os nomes de métodos válidos de um objeto de instância dependem de sua classe. Ou seja, os atributos de uma classe que são objetos de função definem métodos correspondentes de suas instâncias.
"""
