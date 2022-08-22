#quebrando um numero
import math
num = float(input("digite um valor:"))
print("o valor digitado foi {} e a su porção inteira é {}".format(num,math.trunc(num)))

#catetos e hipotenusas
import math
co = float(input("comprimento do cateto oposto?"))
ca = float(input("comrpimento do cateto adjacente?"))
hipo = math.hypot(co,ca)
print("a hipotenusa vai medir {:.2f} ".format(hipo))

#Seno, Cosseno e Tangente
import math
num = float(input("digite o ângulo que você deseja?"))
print("o ângulo de {} tem o seno de {:.2f}".format(num, math.sin(math.radians(num))))
print("o ângulo de {} tem o cosseno de {:.2f}".format(num, math.cos(math.radians(num))))
print("o ângulo de {} tem o tangente de {:.2f}".format(num, math.tan(math.radians(num))))