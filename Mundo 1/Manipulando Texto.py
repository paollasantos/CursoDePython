''''
Manipulando Texto
**** fatiamento ****

frase = " Curso em Video Python "
variavel + [e o numero dentro da str]

frase[9] ele vai identificar dentro da cadeia de cariter, somente o cariter 9
frase[9:13] o ultimo numero ele excluir (o 13 vai pega 12 sempre -1 no final)
frase[9:21:2] vai começa no 9 vai termina no 21 porem vai pulando de 2 em 2
frase[:5] ele começa no cariter 0 e termina no 5
frase[15:] indicou o inicio sem sabe o final
frase[9::6] vai começa no 9 sem o final pulando de 3 em 3
 
**** Análise ****
len(frase) comprimento da frase
frase.count("o") contar quantas vezes aparece a letra o 
frase.find("deo") quantas vezes ele vai encontrar o deo 

****  transformações ****
frase.replace(python,android) troca a palavra python e subitituir andoid
frase.upper() vai fica tudo em maiusculas 
frase.lower() fica tudo em minuscula
frase.capitalize() so  primeira letra da str ficara em maiuscula
frase.title() coloca todas as primeira letras de cada palavra em maiuscula
frase.strip() vai tirar todos os espaços
frase.rstrip() vai tira os espaços da direita
frase.lstrip() vai tira os espaço da esquerda
'''
#exemplos
frase ="curso em video python"
print(frase[5:19:2])
 
frase ="curso em video python"
print(frase.upper().count("O"))

frase = "curso em video python"
print(len(frase))

frase = "curso em video python"
frase = frase.replace("python","android")
print(frase)







