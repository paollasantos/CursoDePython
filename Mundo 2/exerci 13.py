# Cálculo do Fatorial
num = int(input('''Digite um número para
calcular seu fatorial: '''))
c = num
f = 1
print("Calculando {}! = ".format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print("{}".format(f))

#  Progressão Aritmética v2.0
print("GERADOR DE UMA PA")
print('=-' * 10 )
p = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
c = 1
while c <= 10:
    s = p + (c - 1) * r
    c += 1
    print(s, end=" → ")
print("FIM...")

# Super Progressão Aritmética v3.0
print("GERADOR DE UMA PA")
print('=-' * 10 )
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print("{}  → ".format(termo), end='')
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print("Progressão finalizada com {} termos mostrados".format(total))
print("FIM...")

