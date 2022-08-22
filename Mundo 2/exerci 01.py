#   Aprovando Empréstimo 
from time import sleep
casa = float(input("Qual o valor da casa? "))
salário = float(input("Salário do comprador? "))
anos = int(input("Quantos anos de financiamento? "))
print("PROCESSANDO DADOS...")
sleep(2)
prestação = casa / (anos * 12)
if prestação > salário * 0.3:
    print("EMPRÉSTIMO NEGADO!")
else:
    print("EMPRÉSTIMO PODE SER CONCEDIDO!")
print("Para paga uma casa {:.2f}, em {} anos a prestação será {:.2f}!".format(casa,anos,prestação))

#   Comparando números 
p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))
if p > s:
 print("O primeiro número é maior!")
elif s > p:
    print("O segundo número é maior!")
else:
    print("Os dois números são iguais!")


    