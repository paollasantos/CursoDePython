 # Detector de Palíndromo
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(frase,inverso))
if inverso == junto:
     print("É um PALÍNDROMO")
else:
     print("Não é um PALÍNDROMO.")

# Grupo da Maioridade
contmaior = 0
contmenor = 0
from datetime import date
atual = date.today().year
for c in range(1,8):
      nasc = int(input("Em qual ano a {}ª pessoa nasceu? ".format(c)))
      idade = atual - nasc
      if idade > 21:
           contmaior += 1
      else:
           contmenor += 1
print("Ao todo tivermos {} pessoas maior de idade".format(contmaior))
print("E também tivermos {} pessoas menores de idade".format(contmenor))


     
