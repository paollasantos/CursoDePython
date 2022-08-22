'''    >>>>>>  Interrompendo repetições while  <<<<<<
Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.
É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
além disso, vamos aprender como trabalhar com as novas fstrings do Python. ''' 

# antes do break
'''n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))'''

# EXEMPLO:
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

# fstrings
# print('A soma vale {}'.format(s))   --->>>  print(f'A soma vale {s})

# EXEMPLO:

nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}.')

