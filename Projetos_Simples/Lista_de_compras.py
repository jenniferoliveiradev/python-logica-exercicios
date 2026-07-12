print("Lista de compras")
compras = []

while True:
    print("Escolha uma opção:")
    print("Opção 1 - Adicione um item")
    print("Opção 2 - Remova um item")
    print("Opção 3 - Ver lista")
    print("Opção 4 - Sair")

    opcao = input ("Digite um número:")
    if opcao == "1":
        item = input("Digite o item: ")
        compras.append(item)
        print("Item adicionado com sucesso!")
    elif opcao == "2":
        print("Qual item deseja remover?")
        item_remove = input("Digite o nome do item: ")
        if item_remove in compras:
            compras.remove(item_remove)
            print("Item removido!")
        else:
             print("Item não encontrado na lista!")
    elif opcao == "3":
        for item in compras:
            print(item)
        print(f"Total de itens: {len(compras)}")
    elif opcao == "4":
        print("Lista finalizada!")
        break