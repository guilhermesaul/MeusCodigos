lista = []
while True:
    print("*"*45)
    print("MENU DA LISTA NÚMERICA")
    print("*"*45)
    print("0- Sair do programa")
    print("1- Adicionar elemento na lista: ")
    print("2- Remover elemento na lista: ")
    print("3- Ver elementos da lista: ")
    print("4- Ver quantidade de elementos na lista: ")
    print("5- Ver soma de elementos na lista: ")
    print("6- Ver o maior elemento na lista: ")
    print("7- Ver o menor elemento na lista: ")
    print("*"*45)
    o = int(input("Digite o número referente a opção que você deseja executar: "))
    if o == 1:
        lista.append(int(input("Digite o número que você deseja selecionar: ")))
    elif o == 2:
        lista.pop(int(input("Digite o indice que você quer excluir: ")))
    elif o == 3:
        print(lista)
    elif o == 4:
        print(len(lista))
    elif o == 5:
        print(sum(lista))
    elif o == 6:
        print(max(lista))
    elif o == 7:
        print(min(lista))
    elif o == 0:
        print("Encerrando programa...")
        break
    else:
        print("Erro! Digite um número que esteja dentro das opções listadas acima.")