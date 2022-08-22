# Estrutura de repetição while
''' Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.

aula passada:                                agora:
                                (           c = 1
for c in range(1,10):            )          while c < 10:
    print(c)                    (               print(c)      
print("fim")                     )              c += 1   ou c = c + 1
                                (          print("fim")
Por exemplo:
c=1
while c !=10:
    print(c)
    c+=1
print('Acabou') '''

# EXEMPLO 01:
n = 0
while n != 0:
    n = int(input("Digite um valor: "))
print("FIM!")

# EXEMPLO 02:
r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/ N] ")).upper()
print("FIM!")

# EXEMPLO 03:
n = 0
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números impares!".format(par, impar))
