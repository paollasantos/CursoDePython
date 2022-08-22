''' >>>> ESTRUTURA DE REPETIÇÃO <<<<

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for",
que é uma estrutura versátil e simples de entender.

se quiser que conte de tras pra frente tem que coloca {for c in range(0 ,4 -1):}
se quiser contar de 2 em 2 ou mais tem que coloca {for c in range (0, 4,2):}

Por exemplo:
for c in range(0, 4):
     print(c)
print('Acabou') '''

# EXEMPLO 01
n = int(input("Digite um numero:"))
for c in range(0, n+1):
    print(c)
print("fim")
# EXEMPLO 02
i = int(input("inicio:"))
f = int(input("fim:"))
p = int(input("passo:"))
for c in range(i, f+1, p):
    print(c)
print("fim")
#EXEMPLO 03
s = 0
for c in range(0, 3):
    int(input("Digite um valor:"))
    s += n
print("O somatório de todos os valores foi {}.".format(s))