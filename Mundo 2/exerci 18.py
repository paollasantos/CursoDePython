# Estatísticas em produtos
print("==" * 10)
print('LOJA SUPER BARATÃO')
print("==" * 10)
barato = soma = cont = 0
while True:
    produto = str(input("Nome do Produto: "))
    preço = int(input("Preço: R$"))
    soma += preço
    if preço < barato or barato == 0:
        barato = preço
        prod = produto.upper()
    if preço > 1000:
        cont += 1
    co = ' '
    while co not in "SN":
        co = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if co == "N":
        break
print("===== FIM DO PROGRAMA =====")
print(f'''O total da compra foi R${soma:.2f}
Temos {cont} produtos custando mais de R$1000.00
O produto mais barato foi {prod} que custa R${barato:.2f} ''')