# 4.7 - Definindo funções

# Podemos criar uma função que escreve a série de Fibonacci em um limite arbitrário:

def fib(num):
  # Imprima uma série de Fibonacci até n.
    a, b = 0, 1
    while(a < num):
        print(a, end='  ')
        a, b = b, a+b
    print()

# Agora chame a função que acabamos de definir:


print(fib(200))
# output: 0  1  1  2  3  5  8  13  21  34  55  89  144 None

"""
Resumo de Funções no Python:

A palavra-chave 'def' introduz uma definição de função. Deve ser seguido pelo nome da função e a lista entre parênteses de parâmetros formais. As instruções que formam o corpo da função começam na próxima linha e devem ser recuadas.

A execução de uma função introduz uma nova tabela de símbolos usada para as variáveis locais da função. Mais precisamente, todas as atribuições de variáveis em uma função armazenam o valor na tabela de símbolos local; enquanto as referências de variáveis primeiro procuram na tabela de símbolos locais, depois nas tabelas de símbolos locais das funções delimitadoras, em seguida, na tabela de símbolos globais e, finalmente, na tabela de nomes internos. 

Os parâmetros reais (argumentos) para uma chamada de função são introduzidos na tabela de símbolos local da função chamada quando ela é chamada; assim, os argumentos são passados usando 'call by value' (onde o valor é sempre uma referência de objeto, não o valor do objeto). Quando uma função chama outra função, ou chama a si mesma recursivamente, uma nova tabela de símbolos local é criada para essa chamada.
"""

# É simples escrever uma função que retorne uma lista dos números da série de Fibonacci, em vez de imprimi-la, usamos a palavra reservada 'return':


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

1 - A instrução 'return' retorna com um valor de uma função. O 'return' sem um argumento de expressão retorna 'None'. Sair do final de uma função também retorna 'None'.

2 - A instrução 'result.append(a)' chama um método do objeto list result. Um método é uma função que 'pertence' a um objeto e é chamada de 'obj.method_name', onde obj é algum objeto (isso pode ser uma expressão), e methodname é o nome de um método que é definido pelo tipo do objeto.
  
  O método '.append()' mostrado no exemplo é definido para objetos de lista; ele adiciona um novo elemento no final da lista. Neste exemplo é equivalente a 'result = result + [x]', só que mais eficiente.
"""
