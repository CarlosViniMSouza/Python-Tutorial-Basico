num = int(input("Qual o fatorial queres calcular?: "))

fat = 1  # começamos a operação aqui

for i in range(1, num + 1):
    fat = fat * i  # aqui faremos: 1 * 2 * 3 * 4 * ...
    print("fatorial ate agora: ", fat)

print("Seu fatorial eh:", fat)
