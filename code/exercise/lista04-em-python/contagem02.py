contT, soma = 0, 0

num = int(input("Digite um inteiro: "))

while num != 0:
    if num % 2 == 0:
        soma += num
        contT += 1

    elif num % 2 != 0:
        print("\nValores impares nao sao aceitos!\n")

    elif num < 0:
        print("\nPrecisam ser valores positivos!\n")

    num = int(input("\nDigite um inteiro: "))

if num == 0 and soma == 0:
    contT += 1

print("\nOperacao feita!")
print("A media foi:", (soma/contT))
