# Par ou Ímpar?
num = int(input("Me diga um número qualquer: "))
if  ( num % 2 ) == 0:
    print("O número {} é PAR".format(num))
else:
    print("O número {} é IMPAR".format(num))

#  Custo da Viagem
from time import sleep
km = float(input("qual é a distância de sua viagem em km ? "))
print("PROCESSANDO DADOS...")
sleep(2)
v1 = km * 0.5
v2 = km * 0.45
if km <= 200:
    print("Para você realizar a sua viagem de {:.2f}km, terá o custo de R${:.2f}".format(km, v1))
else:
    print("Para você realizar a sua viagem de {:.2f}km, terá o custo de R${:.2f}".format(km, v2))
print("BOA VIAGEM!")

