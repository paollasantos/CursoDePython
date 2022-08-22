# Aumentos múltiplos
salário = float(input("qual é o salário do funcionário? R$"))
if salário <= 1250:
    novo = salário + (salário * 15/100 )
else:
    novo = salário + (salário * 10/100)
print("quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salário, novo))

# Analisando Triângulo v1.0
from time import sleep
print("-==-" * 15)
print("               ANALISANDO TRIÂNGULOS               ")
print("-==-" * 15)
p = float(input("primeiro segmento: "))
s = float(input("segundo segmento: "))
t = float(input("terceiro segmento: "))
print("PROCESSANDO DADOS...")
sleep(2)
if p < s + t and s < p + t and t < p + s:
    print("Os segmentos acima podem forma um triângulo.")
else:
    print("Os segmentos acima não pode forma um triângulo.")      

