#pintando a parede 
largura = float(input("qual é a largura da sua parede?"))
altura = float(input("e a altura?"))
print("sua parede tem a dimensão de {}x{} e a sua área é de {}m²".format(largura,altura,(largura*altura)))
print("para pintar essa parede, você precisará de {}l de tintas".format(largura*(altura/2)))

#calculando descontos
prod = float(input("qual é o preço do produto? R$"))
s1 = prod - (prod * 5 / 100)
print("o produto que custava R${}, na promoção com desconto de 5% vai custar R$ {:.2f}".format(prod, s1))

#reajuste salarial
salário = float(input("qual é o salário do funcionario? R$"))
s = salário + (salário * 15/100)
print("um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(salário,s))

#conversor de temperaturas
temp = float(input("informe a temperatura em ºC:"))
s = (( 9 * temp ) / 5 ) + 32
print("a temperatura de {}ºC corresponde a {}ºF!".format(temp,s))

#aluguel de carro
dias = int(input("quantos dias alugado?"))
km = float(input("quantos km rodados?"))
s = (dias * 60) + (km * 0.15)
print("total a pagar é de R${:.2f}".format(s))
