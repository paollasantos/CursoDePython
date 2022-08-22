 # Vários números com flag
n = s = 0
cont = 0
while True:
    n = int(input("Digite um número: (999 para parar) "))
    if n == 999:
        break
    s += n
    cont += 1
print(f"A soma {cont} valores foi {s}!")

# Tabuada v3.0
n = 0
num = 0
while True:
    print("-" * 45)
    n = int(input("Digite um número para ver a tabuada: "))
    print("-" * 45)
    if n < 0:
        break
    for num in range (0,11):
        print(f"{n} X {num} = {n*num}")
print("PROGRAMA ENCERRADO, VOLTE SEMPRE!")
