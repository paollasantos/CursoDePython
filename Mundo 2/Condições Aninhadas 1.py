'''   >>> ESTRUTURAS DE CONTROLE (Condições Aninhadas) <<<
IF = se 
ELIF = senâo (pode utilizar mais de uma vez)
ELSE = outro senão
'''

# EXEMPLO
nome = str(input("qual é o seu nome? "))
if nome == "paola":
    print("Que nome bonito!")
elif nome == "maria" or nome =="gabriel" or nome == "matheus": 
    print("Seu nome é bem popular no Brasil!") 
elif nome in "ana juliana gabriela isabela":
    print("Belo nome feminino!")
else:
    print("seu nome é bem normal!")
print("tenha um bom dia, {}!".format(nome))