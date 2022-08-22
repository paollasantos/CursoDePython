#sorteando um item da lista
from random import choice
p = input("primeiro aluno:")
s = input("segundo aluno:")
t = input("terceiro aluno:")
q = input("quarto aluno:")
r = [p,s,t,q]
print("a pessoa escolhida foi {}".format(choice(r)))

# Sorteando uma ordem na lista
import random
p = str(input("primeiro aluno:"))
s = str(input("segundo aluno:"))
t = str(input("terceiro aluno:"))
q = str(input("quarto aluno:"))
r = [p,s,t,q]
random.shuffle(r)
print("a ordem de apresentação é:")
print(r)


