lista = []
while True:
    print("*"*45)
    print("MENU DE LISTA DE STRING")
    print("*"*45)
    print("0- Sair do programa")
    print("1- Adicionar nome na lista")
    print("2- Remover nome na lista")
    print("3- Ver lista")
    print("4- Quantidade de elementos na lista")
    print("*"*45)
    op = int(input("Digite o número equivalente ao que você deseja executar: "))
    if op == 0:
        print("Encerrando programa...")
        break
    elif op == 1:
        lista.append(input("Digite o nome que você deseja adicionar: "))
    elif op == 2:
        lista.remove(input("Digite o nome que você deseja remover: "))
    elif op == 3:
        for x in lista:
            print(x)
    elif op == 4:
        print(len(lista))
    else:
        print("Digite uma opção válida")