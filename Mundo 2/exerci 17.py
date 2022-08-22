# Análise de dados do grupo
print('===' * 7)
print("CADASTRE UMA PESSOA")
print('===' * 7)
tot18 = h = m = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo =' '
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        h += 1
    if sexo == "F" and idade < 20:
        m += 1
    co = ' '
    while co not in "SN":
        co = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if co == "N":
        break
print(f'''Total de pessoas com mais de 18 anos: {tot18}
Ao todo temos {h} homens cadastrado
e temos {m} mulheres com menos de 20 anos''')

