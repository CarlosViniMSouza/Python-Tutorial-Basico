"""
Faça um algoritmo que leia o sexo, a idade e a escolaridade (fundamental, médio e superior) e
determine o cargo que a pessoa pode se candidatar, dada a tabela abaixo. O número de pessoas a se
candidatar às vagas é incerto.

(OBS.:A condição de parada é quando a idade da pessoa for menor ou igual a 0)

| Sexo | Idade | Escolaridade |    Cargo       |
|   F  | < 25  |    Médio     | Recepcionista  |
|   M  | > 40  | Fundamental  | Servente       |
|F ou M| < 30  |  Superior    | Auxiliar de RH |
"""

sexo = input("Digite seu sexo: (F - Feminino | M - Masculino): ")
idade = int(input("Qual a sua idade: "))
esco = input("Sua escolaridade (Fundamental, Medio ou Superior): ")

while idade != 0:

    if (sexo == "F") and (idade < 25) and (esco == "Medio"):
        print("\nCargo: Recepcionista\n")

    elif (sexo == "F") and (idade > 40) and (esco == "Fundamental"):
        print("\nCargo: Servente\n")

    elif (sexo == "F" or "M") and (idade < 30) and (esco == "Superior"):
        print("\nCargo: Auxiliar de RH\n")

    else:
        print("Nao temos uma vaga para o seu perfil")

    sexo = input("Digite seu sexo: (F - Feminino | M - Masculino): ")
    idade = int(input("Qual a sua idade: "))
    esco = input("Sua escolaridade (Fundamental, Medio ou Superior): ")

print("Programa Encerrado")
