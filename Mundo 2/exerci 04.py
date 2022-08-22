#   Índice de Massa Corporal
peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / ( altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5 :
    print("Está ABAIXO DO PESO!")
elif imc >= 18.5 and imc < 25 :
    print("PARABÉNS! está o seu PESO IDEAL!")
elif imc >= 25 and imc < 30 :
    print("Está em SOBREPESO!")
elif imc >= 30 and imc < 40 :
    print("Está com OBESIDADE!")
else:
    print("Está com OBESIDADE MÓRBIDA!")

# Gerenciador de Pagamentos
print("{:=^40}".format(" LOJA DA PAOLA "))
preço = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO!
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartâo
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço *  5/100) 
elif opção == 3:
    total = preço 
    parcela = total / 2
    print("Sua compra será parcela em 2x de R${}.".format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparcel = int(input("Quantas parcelas? "))
    parcela = total / totparcel
    print("Sua compra será parcela em {}x de R${}.".format(totparcel, parcela))
else:
    total = 0
    print("OPÇÃO INVÁLIDA de pagamento, tente novamente!")
print("Sua compra de R${:.2f}, vai custar R${:.2f} no final.".format(preço,total))
