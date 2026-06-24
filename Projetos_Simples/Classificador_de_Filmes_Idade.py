print (f"L → Livre \n10 → Maior de 10 anos, \n12 → Maior de 12 anos, \n14 → Maior de 14 anos, \n16 → Maior de 16 anos, \n18 → Maior de 18 anos")

nome_usuario = input("Digite o seu nome: ")
idade_usuario = int(input("Digite a sua idade: "))
classificacao_filme = str(input("Digite a classificação do filme que deseja assistir: "))


if classificacao_filme == "L":
    print (f" Olá {nome_usuario}, você pode assistir a este filme!")
elif classificacao_filme == "10":
    if idade_usuario >= 10:
        print (f" Olá {nome_usuario}, você pode assistir a este filme!")
    else:
        print(f"{nome_usuario}, você não pode assistir. É necessário ter 10 anos.")
elif classificacao_filme == "12":
    if idade_usuario >= 12:
         print (f" Olá {nome_usuario}, você pode assistir a este filme!")
    else:
        print(f"{nome_usuario}, você não pode assistir. É necessário ter 12 anos.")
elif classificacao_filme == "14":
    if idade_usuario >= 14:
        print (f" Olá {nome_usuario}, você pode assistir a este filme!")
    else:
        print(f"{nome_usuario}, você não pode assistir. É necessário ter 14 anos.")
elif classificacao_filme == "16":
    if idade_usuario >= 16:
        print (f" Olá {nome_usuario}, você pode assistir a este filme!")
    else:
        print(f"{nome_usuario}, você não pode assistir. É necessário ter 16 anos.")   
elif classificacao_filme == "18":
    if idade_usuario >= 18:
        print (f" Olá {nome_usuario}, você pode assistir a este filme!")
    else:
        print(f"{nome_usuario}, você não pode assistir. É necessário ter 18 anos.")   
else:
    print (f"Classificação inválida!")