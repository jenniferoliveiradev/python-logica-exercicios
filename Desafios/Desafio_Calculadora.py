numero_1 = int(input("Digit um número: "))
operacao = input("Digite a operação desejada: ")
numero_2 = int(input("Digite o segundo número: "))

if operacao == "+":
    resultado = numero_1 + numero_2 
    print(f"{resultado}")
elif operacao == "-":
    resultado = numero_1 - numero_2 
    print(f"{resultado}")
elif operacao == "*":
    resultado = numero_1 * numero_2 
    print(f"{resultado}")
elif operacao == "/":
        if numero_2 == 0:
            print("Não é possivel dividir por zero!")
        else:
            resultado = numero_1 / numero_2 
            print(f"{resultado}")

else: 
    print(f"Operação invalida!")
