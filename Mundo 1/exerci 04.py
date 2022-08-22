# antecesor e sucessor 
n = int(input("digite um numero: "))
print ("analisando o valor {},o seu antecesor é {} e o seu sucessor é {}".format(n,(n-1),(n+1)))

# dobro, triplo e raiz quadrada 
n = int(input("digite um numero: "))
print("o dobro de {} será {}".format(n, (n*2)))
print("o triplo de {} será {}".format(n, (n*3)))
print("a raiz de {} quadrada será {:.2f}".format(n, (n**(1/2)))) 

# média aritmética 
n1 = float(input("primeira nota do aluno: "))
n2 = float(input("segunda nota do aluno: "))
m = (n1+n2)/2
print ("a média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1,n2,m)) 

#convesor de medidas
medida = float(input("uma distancia em metros:"))
mm = medida / 1000
cm = medida / 100
dm = medida / 10
dan = medida * 10
hm = medida * 100
km = medida * 1000
print ("a sua medida em mm é {},em cm {}, em dm {},em dan {},em hm {}, e em km {} correto? ".format(mm,cm,dm,dan,hm,km))
