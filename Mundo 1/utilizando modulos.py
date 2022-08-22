'''
da para utilizar = import 'math'   ou   from 'math' import 'sqrt'
dentro da biblioteca tem varios modulos = exemplo = math (matematica)
e dentro do modulo varias expressões, EXEMPLO
ceil       =    arendodamento para cima
floor      =    arrendodamento pra baixo
trunc      =    truca o numero - elimina da , pra frente sem arrendodamento 
pow        =    potencia
sqrt       =    raiz quadrada 
factorial  =    fatorial

#exemplo
import math
num = int(input("digite um numero:"))
raiz = math.sqrt(num)
print("a raiz de {} é igual a {}".format(num, math.ceil(raiz)))'''

#exemplo
import random
num = random.randint(1, 10)
print(num)
