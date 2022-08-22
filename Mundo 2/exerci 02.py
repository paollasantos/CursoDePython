#    Alistamento Militar
from datetime import date
nasc = int(input("Ano do seu nascimento?"))
atual = date.today().year
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
saldo = idade - 18
saldo2 = 18 - idade
if idade > 18:
    print("Você ja deveria ter se alistado há {} anos!!".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi {} ano!!".format(ano))
elif idade == 18:
    print("Já está na hora de se alistar!")
elif idade < 18:
    print("Ainda faltam {} anos para você se alistar!!".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será {} ano.".format(ano))