#Analisador de Textos
nome = str(input("digite o seu nome completo:"))
print("analisando o seu nome...")
print("seu nome em maiusculas é {}".format(nome.upper()))
print("seu nome em minusculas é {}".format(nome.lower()))
print("seu nome ao todo tem {} letras".format(len(nome)-nome.count(" ")))
print("seu primeiro nome tem {} letras".format(nome.find(" ")))
  
# Separando dígitos de um número
numero = int(input("informe um numero de 0 á 9999 : "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("anaisando o numero {}".format(numero))
print("a sua unidade é {}".format(u))
print("a sua dezena é {}".format(d))
print("a sua centena é {}".format(c))
print("a sua milhar é {}".format(m))

#Verificando as primeiras letras de um texto  
cidade = str(input("em qual cidade você nasceu?")).lower() .strip()
print("santo" in cidade)

#Procurando uma string dentro de outra 
nome = str(input("qual é seu nome completo:")).lower() .strip()
print("seu nome tem silva? {}".format("silva" in nome))
