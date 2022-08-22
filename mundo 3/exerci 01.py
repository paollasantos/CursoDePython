# Número por Extenso
sequencia = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove','dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num not in range(0,21):
    num = int(input('''TENTE NOVAMENTE! 
Digite um número entre 0 e 20: '''))
print(f'Você digitou o número {sequencia[num]}') 


# Tuplas com Times de Futebol
lista = ('Corithians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco',
'Chapecoense','Atlético','Botafogo','Athético PR','Bahia','São Paulo','Fluminense',
'Sport Recufe','EC Vitória','Curitiba','Avaí','Ponte Preta','Atlético GO')
print('-=-' * 25)
print(f'LISTA DE TIMES DO BRASILEIRÃO: {lista}')
print('-=-' * 25)
print(f'Os 5 primeiros são {lista[0:5]}')
print('-=-' * 25)
print(f'Os 4 últimos são {lista[-4:]}')
print('-=-' * 25)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-=-' * 25)
print(f'O Chapecoense esta na {lista.index("Chapecoense")+1}ª posição')