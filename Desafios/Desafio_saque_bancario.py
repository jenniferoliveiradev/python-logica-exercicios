saldo_conta = float(input("Digite o seu saldo: "))
valor_saque = float(input("Digite o valor que deseja sacar: "))
valor_saldo  = saldo_conta - valor_saque


if saldo_conta >= valor_saque:
    print(f"Saque realizado! Seu saldo é: R$ {valor_saldo: .2f}")
else: 
    print(f"Saldo insuficiente! Seu saldo é: R$ {valor_saldo: .2f}")
