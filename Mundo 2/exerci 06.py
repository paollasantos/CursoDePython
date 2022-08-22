#  Contagem regressiva 
from time import sleep
print("CONTAGEM REGRESSIVA")
for c in range(10, -1,-1):
    print(c)
    sleep(0.5)
print("BUM! BUM! POOOW!")

# Contagem de pares 1 a 50
for num in range(0, 50+1):
    if ( num % 2 ) == 0:
        print(num, end = " ")

#  Soma ímpares múltiplos de três
s = 0
c = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        s += num
        c += 1
print("A soma de todos os {} valores solicitados {}".format(c, s))
