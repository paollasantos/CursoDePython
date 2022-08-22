# Simulador de Caixa Eletrônico
print("=-=" * 4)
print(" BANCO CEV")
print("=-=" * 4)
while True:
    saque = float(input("Que valor você quer sacar? R$ "))
    for cédulas in [50,20,10,1]:
        quantidade = saque // cédulas
        saque = saque % cédulas
        if quantidade > 0:
            print(f"Total de {quantidade:.0f} cédulas de R${cédulas}")
    print("=-=" * 12)


