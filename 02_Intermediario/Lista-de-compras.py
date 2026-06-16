print("Lista de compras: ")
compras = []

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        while True:
            item = input("Digite o nome do item ou sair para voltar ao menu: ").lower()
            if item == "sair":
                break
            compras.append(item)
            print(f"{item} adicionado à lista de compras.")

    elif opcao == "2":
        if len(compras) == 0:
            print("Sua lista de compras está vazia.")
        else:
            print("\nSua lista de compras:")
            for i, item in enumerate(compras, start=1):
                print(f"{i}. {item}")

    elif opcao == "3":
        print("Encerrando o programa. Até mais!")
        break