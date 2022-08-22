#   Jogo da Adivinhação
import random
from time import sleep
num = random.randint(0,5)
print("--=--" * 20 )
print("vou pensar em um número entre 0 e 5. tente adivinhar...")
print("--=--" * 20 )
n = int(input("em que número pensei? "))
print("PROCESSANDO...")
sleep(2)
print(num)
if n == num:
    print("acertou miseraviiii!!")
else:
    print("perdeu playboy!!!")

#  Radar eletrônico ( A multa vai custar R$7,00 por cada Km acima do limite)
from random import randint
from time import sleep
print("-=-" * 10)
print( "seu carro passou no radar...")
print( "-=-" * 10 )
sleep(2)
vel = randint(10,180)
if vel > 80:
     print("MULTADO! Você estava á {}km/h por tanto excedeu o limite permitido que é 80km/h, você deve pagar uma multa de R${:.2f}".format(vel, (vel - 8 * 7)))
else:
     print("você estava á {}km/h por tanto continue respeitando os limites de velocidade!".format(vel))
print("tenha um bom dia, Dirija com segurança!!")
