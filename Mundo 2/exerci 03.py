 #  Aquele clássico da Média
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
m = ( n1 + n2 ) / 2
if m < 5.0:
    print("A sua média foi {:.1f} entretando foi REPROVADO!".format(m))
elif m >= 7.0:
    print("A sua média foi {:.1f}, Parabens,APROVADO!".format(m))
elif m >= 5.0 and m < 7:
    print("A sua média foi {:.1f} entretando está em RECUPERAÇÂO!".format(m))

#  Classificando Atletas
from datetime import date
nasc = int(input("Qual é o ano do seu nascimento? "))
atual = date.today().year
idade = atual - nasc
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("CLASSIFICAÇÃO: MIRIM")
elif idade <= 14:
    print("CLASSIFICAÇÃO: INFANTIL")
elif idade <= 19:
    print("CLASSIFICAÇÃO: JÚNIOR")
elif idade <= 25:
    print("CLASSIFICAÇAO: SÊNIOR")
elif idade > 25:
    print("CLASSIFICAÇÂO: MASTER")
    