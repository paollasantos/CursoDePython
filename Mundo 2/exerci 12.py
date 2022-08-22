# Criando um Menu de Opções
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Agora o segundo valor: '))
opção = 0
while opção != 5:
    print("""      MENU
    -------------------------   
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    -------------------------""")
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        somar = n1 + n2
        print("A soma entre {} e {} será {}".format(n1,n2,somar))
    elif opção == 2:
        multiplicação = n1 * n2
        print("A multiplicação entre {} e {} será {}".format(n1,n2,multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior é {}".format(n1,n2,maior))
    elif opção == 4:
        print("informe os números noamente:")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Agora o segundo valor: "))
    elif opção == 5:
        print("PROGRAMA ENCERRADO...")
    else:
        print("OPÇÃO INVALIDO, TENTE NOVAMENTE!")
        print("=-=" * 10 )
print("Fim do programa, volte sempre !")
