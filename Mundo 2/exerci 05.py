 # GAME: Pedra Papel e Tesoura
from time import sleep
from random import randint
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
sleep(2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
sleep(2)
computador = randint(0,2)
if jogador == 0 and computador == 1:
    print("--=--" * 8 )
    print('''     Jogador jogou, PEDRA
    e o computador jogou, PAPEL.''') 
    print("--=--" * 8 )
    print('''     PERDEU PLAYBOY,
    O computador VENCEU!!''')
elif jogador == 0 and computador == 2:
    print("--=--" * 8 )
    print('''     Jogador jogou, PEDRA
    e o computador jogou, TESOURA.''')
    print("--=--" * 8 )
    print('''     ACERTOU MISERAVIIII,
    O jogador VENCEU!!''')
elif jogador == 1 and computador == 0:
    print("--=--" * 8 )
    print('''     Jogador jogou, PAPEL
    e o computador jogou, PEDRA.''')
    print("--=--" * 8 )
    print('''     ACERTOU MISERAVIIII,
    O jogador VENCEU!!''')
elif jogador == 1 and computador == 2:
    print("--=--" * 8 )
    print('''     Jogador jogou, PAPEL
    e o computador jogou TESOURA.''')
    print("--=--" * 8 )
    print('''     PERDEU PLAYBOY,
    O computador VENDEU!!''')
elif jogador == 2 and computador == 0:
    print("--=--" * 8 )
    print('''     Jogador jogou, TESOURA,
    e o computador jogou, PEDRA.''')
    print("--=--" * 8 )
    print('''     PERDEU PLAYBOY,
    O computador VENDEU!!''')
elif jogador == 2 and computador == 1:
    print("--=--" * 8 )
    print('''     Jogador jogou, TESOURA
    e o computador jogou, PAPEL.''')
    print("--=--" * 8 )
    print('''     ACERTOU MISERAVIIII,
    O jogador VENCEU!!''')
else:
    print('''     DEU EMPATE
     tente novamente!!''')

