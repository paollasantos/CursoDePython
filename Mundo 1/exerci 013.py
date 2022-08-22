# Ano Bissexto
from datetime import date
from time import sleep
from calendar import isleap
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atua: "))
print("PROCESSANDO...")
sleep(2)
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))

# Maior e menor valores
from time import sleep
p = int(input("digite o primeiro valor:"))
s = int(input("digite o segundo valor:"))
t = int(input("digite o terceiro valor:"))
num = [p,s,t]
print("PROCESSANDO DADOS...")
sleep(2)
print("o menor valor digitado é {}".format(min(num)))
print("o maior valor digitado é {}".format(max(num)))

