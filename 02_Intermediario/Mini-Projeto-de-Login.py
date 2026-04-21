usuario = "admin"
senha = "python123"

for i in range(3):
    temtativa_usuario = input("Digite o usuario: ")
    temtativa_senha = input("Digite a senha: ")
    if temtativa_usuario == usuario and temtativa_senha == senha:
        print(f"Acesso Permitido: \nSeja Bem-Vindo {usuario}")
        break
    else:
        if i < 2:
            print(f"Dados Incorretos. Você tem {2 - i} tentativas. ")
        else:
             print("Senha Invalida! Procure a gerencia.")
