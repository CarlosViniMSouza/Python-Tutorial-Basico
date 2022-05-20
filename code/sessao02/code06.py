# 4.7 - Funções

# Podemos criar uma função que escreve a série de Fibonacci até certo ponto:

def fib(num):
  # Imprima uma série de Fibonacci até n.
    a, b = 0, 1
    while(a < num):
        print(a, end='  ')
        a, b = b, a+b

# Agora chame a função que acabamos de definir:


print(fib(200))
# output: 0  1  1  2  3  5  8  13  21  34  55  89  144  None

"""
Resumo de Funções no Python:

COMO FUNCIONA: A palavra-chave 'def' introduz uma definição de função. Deve ser seguido pelo nome da função e a lista entre parênteses de parâmetros formais. As instruções que formam o corpo da função começam na próxima linha e devem ser recuadas.

Todas as atribuições de variáveis em uma função armazenam o valor na tabela de símbolos local; enquanto as referências de variáveis primeiro procuram na tabela de símbolos locais, depois nas tabelas de símbolos locais das funções delimitadoras, em seguida, na tabela de símbolos globais e, finalmente, na tabela de nomes internos.

Os parâmetros reais (argumentos) para uma chamada de função são introduzidos na tabela de símbolos local da função chamada quando ela é chamada.

Quando uma função chama outra função, ou chama a si mesma recursivamente, uma nova tabela de símbolos local é criada para essa chamada.

É simples escrever uma função que retorne uma lista dos números da série de Fibonacci, em vez de imprimi-la, usamos a palavra reservada 'return':
"""


def fibonnacci(num):
    result = []
    a, b = 0, 1

    while(a < num):
        result.append(a)
        a, b = b, a+b

    return result


print(fibonnacci(100))
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
Este exemplo, demonstra alguns recursos do Python:

1 - A instrução 'return' retorna com um valor de uma função. O 'return' sem um argumento de expressão retorna 'None'. A saída de uma função podem retornar 'None'.

2 - A instrução 'result.append(a)' - Um método é uma função que 'pertence' a um objeto.
  
  O método '.append()' mostrado no exemplo é definido para objetos de lista; ele adiciona um novo elemento no final da lista. Neste exemplo é equivalente a 'result = result + [x]', só que mais eficiente.
"""
