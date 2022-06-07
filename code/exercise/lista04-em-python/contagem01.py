contM, contF, contT = 0, 0, 0

sexo = input("Seu sexo(m = masculino | f = feminino): ")

while sexo == "m" or sexo == "f":
    if sexo == "m":
        contM += 1
        contT += 1
    else:
        contF += 1
        contT += 1

    sexo = input("Seu sexo(m = masculino | f = feminino): ")

# saindo do laco de repeticao

print("\nTotal de Homens:", contM)
print("Total de Mulheres:", contF)
print("\n(%) Homens:", round((contM/contT)*100, 2), "%")
print("(%) Mulheres:", round((contF/contT)*100, 2), "%")
