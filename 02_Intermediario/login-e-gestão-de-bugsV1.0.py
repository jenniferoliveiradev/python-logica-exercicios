lista_de_bugs = []

while True:
    dados = input("Ja tem conta ou quer se cadastrar?").lower()
    if dados == "cadastrar":
        usuario = input("Digite o nome de usuario: ")
        senha = (input("Digite a senha: "))
        print("Cadastro realizado com sucesso!")
        break
    
for i in range(3):
    tentativa_usuario = input("Digite o usuario: ")
    tentativa_senha = input("Digite a senha: ")
    if tentativa_usuario == usuario and tentativa_senha == senha:
        print(f"Acesso Permitido: \nSeja Bem-Vindo {usuario}")
            
        while True:
            print("Menu.")
            print("1. Adicionar Bug \n2. Ver lista de Bugs \n3. Sair. \n4. Limpar todos os bugs.")
            opcao = (input("Escolha um número: "))
            if opcao == "1":
                erro = input("Qual erro você encontrou?")
                lista_de_bugs.append(erro)
            elif opcao == "2":
                if lista_de_bugs:
                    for bug in lista_de_bugs:
                        print(bug)
                else:
                    print("Nenhum Bug cadastrado ainda.")
            elif opcao == "3":
                break
            elif opcao == "4":
                lista_de_bugs.clear()

        break    
    else:
        if i < 2:
            print(f"Dados Incorretos. Você tem {2 - i} tentativas. ")
        else:
             print("Senha Invalida!")

        