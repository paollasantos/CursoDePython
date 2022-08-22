# TUPLAS 

'''o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis
 que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''
 # Tuplas são IMUTÁVEIS

#EXEMPLOS 
# tres formas de resolver

lanche = ("Hambúrguer","suco","pizza","pudim")
#print(lanche[2]) -- ou -- print(len(lanche)) 

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}") # para mostra a posição so coloca {cont}
print("comi pra caramba")
#          ou
for comida in lanche:
    print(f"eu vou comer {comida}")
print("comi pra caramba")
#          ou
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("comi pra caramba")

lanche = ("Hambúrguer","suco","pizza","pudim") 
print(sorted(lanche))
