#  Tabuada v.2.0
n = int(input("Digite um número para ver a tabuada: "))
print("-=" * 10)
for num in range(0, 11):
   print("{} X {} = {}".format(n , num, n*num))
print("-=" * 10)

# Soma dos pares
s = 0
c = 0
for num in range(1, 7):
   num = int(input("Digite um valor: "))
   if num % 2 == 0:
       s += num
       c += 1
print("Você informou {} numeros pares, e a soma entre eles deu {}".format(c, s))

# Progressão Aritmética
print("==" * 15 )
print("  10 TERMOS DE UMA PA  ")
print("==" * 15 )
p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
for c in range(1,11):
   s = p + (c - 1) * r
   print( s, end= " > ")
print("ACABOU")
