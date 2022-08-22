# Jogo do Par ou Ímpar
from random import randint
print("-=" * 12)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=" * 12)
v = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0,10)
    tipo = ' '
    while tipo not in "PpIp":
       tipo = str(input("Par ou Ímpar? [P/I] ")).strip() .upper() [0]
    total = jogador + computador
    print(f"Você jogou {jogador} e o cumputador {computador}, o total deu {total},", end= " ")
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print("VOCÊ VENCEU !!")
            v += 1
        else:
            print("VOCÊ PERDEU !!")
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print("VOCÊ VENCEU !!")
            v += 1
        else:
            print("VOCÊ PERDEU !!")
            break
    print("Vamos jogar novamente!!")
print(f'''GAMER OVER !!
você venceu {v} vezes''')

        
