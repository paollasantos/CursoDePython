# Números primos
num = int(input("Digite um numero: "))

cont = 0 # CONT É O CONTADOR, SE INICIA COM ZERO

for c in range(1, num+1):
     if num % c == 0:
         # RESULTADO DA DIVISÃO IGUAL A ZERO,SALVA O NUMERO EM AMARELO
         print("\033[33m", f"{c}", end=" ")
         cont += 1 # OU CONT = CONT + 1
     else:
         # RESULTADO DIFERENTE DE ZERO, SALVA O NUMERO EM VERMELHO
         print("\033[31m", f"{c}", end= " ")

print(f"\n\033[m O numero {num} foi divisivel {cont} vezes")

if cont == 2:
    print("ELE É PRIMO")
else:
    print("ELE NÃO É PRIMO")
