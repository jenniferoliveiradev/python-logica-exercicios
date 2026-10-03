estoque = {
"calça":  {"Quantidade": 15, "Preço": 99.99, "Categoria": "Vestuario"},
"casaco": {"Quantidade": 10, "Preço": 119.99, "Categoria": "Vestuario"},
"boné" : {"Quantidade": 6, "Preço": 7.99, "Categoria": "Vestuario"},
}

while True:
    print("\n--- SISTEMA DE ESTOQUE ---")
    print("1. Consultar item")
    print("2. Cadastrar item")
    print("3. Verificar estoque")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        consultar_item = input("Digite o nome do item: ").lower()
        if consultar_item in estoque:
            print(f"O {consultar_item.title()} tem em estoque: {estoque[consultar_item]["Quantidade"]} com o valor: R$ {estoque[consultar_item]["Preço"]}")
        else:
            cadastro_item = input("Item não encontrado. Deseja cadastrar o item? (Sim/Não): ").lower()
            if cadastro_item == "sim":
                qtd_item = int(input("Qual a quantidade? "))
                valor_item = float(input("Qual o valor do item? "))
                categoria_item = input("Qual a categoria do item? ")
                estoque[consultar_item] = {"Quantidade": qtd_item, "Preço": valor_item, "Categoria": categoria_item}
                print("Item cadastrado com sucesso!")

            
    elif opcao == "2":
            cadastro_novo = input("Digite o nome do item: ").lower()
            qtd_item = int(input("Qual a quantidade? "))
            valor_item = float(input("Qual o valor do item? "))
            categoria_item = input("Qual a categoria do item? ")
            estoque[cadastro_novo] = {"Quantidade": qtd_item, "Preço": valor_item, "Categoria": categoria_item}
            print("Item cadastrado com sucesso!")
    elif opcao == "3":
         print(estoque)
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida!")