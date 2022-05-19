# 9.5 - Herança

# LINK: https://docs.python.org/3/tutorial/classes.html#inheritance

"""
É claro que um recurso de linguagem não seria digno do nome "classe" sem oferecer suporte à herança. A sintaxe para uma definição de classe derivada é assim:
"""


class BaseClassName:
    pass


class DerivedClassName(BaseClassName):
    """
    <statement-1>
    ...
    <statement-N>
    """
    pass


"""
O nome 'BaseClassName' deve ser definido em um escopo contendo a definição de classe derivada. No lugar de um nome de classe base, outras expressões arbitrárias também são permitidas. 

Isso pode ser útil, por exemplo, quando a classe base é definida em outro módulo:
"""

# Ex. => class DerivedClassName(modname.BaseClassName):

"""
A execução de uma classe derivada prossegue da mesma forma que para uma classe base. Quando o objeto de classe é construído, a classe base é lembrada. 

Isso é usado para resolver referências de atributos: se um atributo solicitado não for encontrado na classe, a pesquisa prossegue para procurar na classe base.

Essa regra é aplicada recursivamente se a própria 'classe base' for derivada de alguma outra classe.
"""

"""
Python tem duas funções internas que funcionam com herança:

1 - Use '.isinstance()' para verificar o tipo de uma instância: 'isinstance(obj, int)' será True somente se 'obj.__class__' for int ou alguma classe derivada de int.

2 - Use '.issubclass()' para verificar a herança de classe: 'issubclass(bool, int)' é True já que bool é uma subclasse de int. No entanto, issubclass(float, int) é False, pois float não é uma subclasse de int.
"""

"""
- Herança múltipla

Python também suporta uma forma de herança múltipla. Uma definição de classe com várias 'classes base' se parece com isso:
"""


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass

# apenas declarei essas 3 classes de cima para o VS Code desativar o alerta de "Base(N) is not defined Pylance"


class DerivedClassName(Base1, Base2, Base3):
    """
    <statement-1>
    ...
    <statement-N>
    """
    pass


"""
Caso um atributo não seja encontrado em 'DerivedClassName', ele será procurado em Base1, depois (recursivamente) nas sub-classes da Base1, e se não foi encontrado lá, será procurado na Base2, e assim sucessivamente.

Na verdade, é um pouco mais complexo do que isso; a ordem de resolução do método muda dinamicamente para suportar chamadas cooperativas para 'super()'.

Essa abordagem é conhecida em algumas outras linguagens de herança múltipla como 'call-next-method' e é mais poderosa que a 'super chamada' encontrada em linguagens de herança única.

A ordenação dinâmica é necessária porque todos os casos de herança múltipla exibem um ou mais relacionamentos de diamante. Por exemplo, todas as classes herdam do objeto, portanto, qualquer caso de herança múltipla fornece mais de um caminho para alcançar o objeto.
"""

"""
Ok, isso é bem teórico e um pouco complexo de enteder. Portanto, precisarei dar uma melhorada no conteúdo! Agora, vamos começar logo a parte de Módulos para eu começar a me preocupar com simplificação. 
"""
