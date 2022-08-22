# Validação de Dados
sexo = str(input("Informe seu sexo: [F/M] ")).strip() .upper()[0]
while sexo not in 'FfMm':
    sexo = str(input("DADO INVÁLIDO! Tente novamente, informe seu sexo: [F/M] ")).strip() .upper()[0]
print("DADO ADICIONADO COM SUCESSO!!")

#  Jogo da Adivinhação 2.0
import random
computador = random.randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 à 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Tente um número MAIOR!")
        elif jogador > computador:
            print("Tente um número MENOR!")
print("Parabéns! acertou com {} tentativas.".format(palpite))
