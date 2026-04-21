usuario_cadastrado = "admin"
senha_cadastrada = "python123"

print(" Sistema de Acesso ")

for i in range(3):
    tentativa_usuario = input("Digite o usuario: ")
    tentativa_senha = input("Digite a senha: ")
    
    if tentativa_usuario == usuario_cadastrado and tentativa_senha == senha_cadastrada:
        print(f"Acesso Permitido: \nSeja Bem-Vindo {usuario_cadastrado}")
        break
    else:
        if i < 2:
            print(f"Dados Incorretos. Você tem {2 - i} tentativas. ")
        else:
             print("Senha Invalida! Procure a gerencia.")