# Maior e menor valores em Tupla
from random import sample
num= tuple(sample(range(10),5))
print(f'Os valores sorteados foram: {num}')
print(f'''O maior valor sorteado foi: {max(num)}
O menor valor sorteado foi: {min(num)}''')

#  Análise de dados em uma Tupla
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
 
tupla = (a,b,c,d)
tuplax = tupla
cont = pares = 0 
print(f'Você digitou os valores: {tupla}.')
for igual in tupla:
    if igual == 9:
        cont += 1

print(f'O valor 9 apareceu {cont} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3)+1}º posição.')
else:
    print('Não contém número 3.')

for tuplax in tupla:
    if tuplax % 2 == 0:
        pares += 1

print(f'Os valores pares digitados foram {pares}.')
