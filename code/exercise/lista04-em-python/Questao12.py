n = int(input('Digite o número de linhas: '))

impar = -1
par = 0

print("Primeiros pares: ")
for i in range(n):
    par += 2
    print(par, end=" ")

print("\n")

print("Primeiros impares: ")
for i in range(n):
    impar += 2
    print(impar, end=" ")
