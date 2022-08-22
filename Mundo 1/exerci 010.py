# Primeira e última ocorrência de uma string
frase = str(input("digite uma frase:")).lower() .strip()
print("a letra A aparece {} vezes na frase.".format(frase.count("a")))
print("a primeira letra A apareceu na posição {} ".format(frase.find("a")+1))
print("a ultima letra A aparece na posição {}".format(frase.rfind("a")+1))

#Primeiro e último nome de uma pessoa
nome = str(input("digite o seu nome completo:")).lower() .strip()
print("muito prazer em te conhcer!")
print("seu primeiro nome é {}".format(nome.split()[0]))
print("seu ultimo nome é {}".format(nome.split()[-1]))