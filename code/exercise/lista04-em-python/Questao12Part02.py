num = int(input("Digite valor: "))

print("Numeros pares: ")
for i in range(2, (2*num)+1, 2):
    print("Valor atual: ", i)
    # print(i, end=" ")

print("\nNumeros impares: ")
for j in range(1, (2*num), 2):
    print(j, end=" ")
