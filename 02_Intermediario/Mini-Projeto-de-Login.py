usuario = "admin"
senha = "python123"

for i in range(3):
    tentativa_usuario = input("Digite o usuario: ")
    tentativa_senha = input("Digite a senha: ")
    if tentativa_usuario == usuario and tentativa_senha == senha:
        print(f"Acesso Permitido: \nSeja Bem-Vindo {usuario}")
        break
    else:
        if i < 2:
            print(f"Dados Incorretos. Você tem {2 - i} tentativas. ")
        else:
             print("Senha Invalida! Procure a gerencia.")
