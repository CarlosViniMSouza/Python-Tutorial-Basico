linha = int(input("Quantas linhas?: "))

for i in range(1, linha + 1):
    num = 1
    for j in range(1, i + 1):
        print(num, end='\t')
        num += 1
    print()  # começa outra linha
