# estrutura de repetição while()

"""
Por algum motivo, não estou conseguindo encontrar a documentação desse comando, portanto, farei o material dele com o meu conhecimento prévio.

Resumidamente, o while() é uma estrutura de repetição que recebe uma condição como parâmetro (tanto para iniciar a execução do código, quanto para finalizar a execução).

E cuidado, caso você insira uma condição que nunca será satisfeita, o código entrará em loop infinito! Exemplo:

```
var = 10

while(var > 5):
  print(var)
```

Nesse trecho mencionado acima, o interpretador do Python irá imprimir o número 10 eternamente (a menos que você cancele o processo). Vamos a um exemplo mais dinâmico:
"""

quantia = int(input("Insira quanto dinheiro tens no momento: "))
cont_notas = 0

while(quantia >= 100):
    quantia -= 100
    cont_notas += 1

print(f"Você precisara de {cont_notas} de R$100")

# zerar contador para reutilizar
cont_notas = 0

while(quantia >= 50):
    quantia -= 50
    cont_notas += 1

print(f"Você precisara de {cont_notas} de R$50")

# zerar contador para reutilizar
cont_notas = 0

while(quantia >= 20):
    quantia -= 20
    cont_notas += 1

print(f"Você precisara de {cont_notas} de R$20")

# zerar contador para reutilizar
cont_notas = 0

while(quantia >= 10):
    quantia -= 10
    cont_notas += 1

print(f"Você precisara de {cont_notas} de R$10")

# zerar contador para reutilizar
cont_notas = 0

while(quantia >= 5):
    quantia -= 5
    cont_notas += 1

print(f"Você precisara de {cont_notas} de R$5")

# OBS.: Esse codigo eu tirei de uma questão da lista 02.

# No momento, só colocarei isso, agora verei como proceder na sessao 02!!
