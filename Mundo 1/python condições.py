'''           
>>>>    Condições    <<<<
Condições simples

(se) if carro.esquerda():    bloco true
(senão) else:                bloco false

se tiver só o if é condição simples
e se tiver o if e o else é condição composta

EXEMPLO
tempo = int(input("quantos anos tem o seu carro?))
if tempo <=3:
    print("carro novo")
else:
    print("carro velho")
print("--fim--")

condição simplificada
tempo = int(input("quantos anos tem o seu carro ?"))
print("carro novo" if tempo <=3 else"carro velho")
print("---fim---")
'''
nome = str(input("qual é o seu nome? "))
if nome == "Paola":
    print("que nome lindo você tem!")
else:
    print("seu nome é tão normal! ")
print("bom dia {}!".format(nome))

n1 = float(input("digite sua primeira nota: "))
n2 = float(input("digite a sua segunda nota:"))
m = (n1 + n2)/2
print("a sua média foi {:.1f}".format(m))
if m >=6.0:
    print("sua média foi boa, parabéns!")
else:
    print("sua média foi ruim,estude mais!")