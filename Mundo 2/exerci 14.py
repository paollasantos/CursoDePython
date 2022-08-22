# Sequência de Fibonacci v1.0
print("--" * 12)
print("SEQUÊNCIA DE FIBONACCI")
print("--" * 12)
termos = int(input("Quantos termos você quer mostrar? "))
cont = 1
anterior = 0
proxima = 1 
soma = 1
while cont <= termos:
    print("{} → ".format(anterior) , end="")
    cont +=1
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
print("FIM...")

# Tratando vários valores v1.0
cont = 0
num = 0
total = 0
while num != 999:
    num = int(input("Digite um número [ 999 para parar ]: "))
    if num != 999:
        cont += num
print("Você digitou alguns números e a soma entre eles é {}".format(cont))

#Maior e Menor valores
n = int(input("Digite um número: "))
r = str(input("Quer continuar? [S/N] ")).upper() .strip() [0]
maior = menor = n
cont = 1 
soma = n
while r != "N":
    n = int(input("Digite um número: "))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = str(input("Quer continuar? [S/N] ")).upper() .strip() [0]
print("Você digitou {} números e a média foi {}".format(cont, soma/cont))
print("O maior valor foi {} e o menor foi {}".format(maior,menor))
