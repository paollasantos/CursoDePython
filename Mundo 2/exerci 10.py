# Maior e menor da sequência
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso lido foi de {}Kg'.format(menor))
print('O maior peso lido foi de {}Kg'.format(maior))
 
# Analisador completo
media = 0
velho = 0
nvel = ''
mulheres = 0
somadaidade = 0
for p in range(1,5):
    print("---- {}ª PESSOA ----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F/M]: ")).strip()
    somadaidade += idade
    if p == 1 and sexo in'Mm':
        velho = idade
        nvel = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nvel = nome
    if sexo in 'Fm' and idade < 20:
        mulheres += 1
media = somadaidade / 4
print("A média de idade do grupo é de {} anos.".format(media))
print("O homem mais velho é {} e  tem {} anos.".format(nvel, velho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(mulheres))

