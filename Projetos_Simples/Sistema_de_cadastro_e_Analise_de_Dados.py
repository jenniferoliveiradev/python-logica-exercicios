nomes = []
cargos = []
salarios = []
funcionarios = []


while True:
    print("Escolha uma Opção: \n Opção 1 - Cadastrar funcionario, \n Opção 2 - Listar funcionários, \n Opção 3 - Analise de dados, \n Opção 4 - Sair.")
    opcao = input("Digite uma opção:")

    if opcao == "1":
        nome = input("Digite o nome do funcionario: ")
        cargo = input("Digite o cargo: ")
        salario = float(input("Digite o salário: "))
        nomes.append(nome)
        cargos.append(cargo)
        salarios.append(salario)
        print("Dados adicionados com sucesso!")

    elif opcao == "2":
       for i in range(len(nomes)):
            print(f"Nome: {nomes[i]} | Cargo: {cargos[i]} | Salário: R${salarios[i]:.2f}")
    elif opcao == "3":
        maior_salario = salarios.index(max(salarios))
        maior_nome = nomes[maior_salario]
        valor_maior = max(salarios)
        menor_salario = salarios.index(min(salarios))
        menor_nome = nomes[menor_salario]
        valor_menor = min(salarios)
        media_salarial = sum(salarios) / len(nomes)
        total_pagamento = sum(salarios)
        print(f"O maior Salário é do(a): {maior_nome}, ganhando: R${valor_maior:.2f}")
        print(f"O menor Salário é do(a): {menor_nome}, ganhando: R${valor_menor:.2f}")
        print(f"A média salária é: {media_salarial:.2f}")
        print(f"O total da folha de pagamento é: {total_pagamento:.2f}")

    elif opcao == "4":
        print("Sistema Finalizado!")
        break
    else:
        print("Opção invalida!")    