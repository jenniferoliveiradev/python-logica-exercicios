print("Preencha os dados abaixo")

usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print ("Login bem-sucedido!")
    
else:
    print("Login falhou! Verifique seu nome de usuário e senha.")
