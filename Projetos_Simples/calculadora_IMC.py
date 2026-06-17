nome_usuario = input("Digite o seu nome: ")
kg_usuario = float(input("Digite o seu peso: "))
altura_usuario = float(input("Digite a sua altura: "))

imc = kg_usuario / (altura_usuario * altura_usuario)

if imc < 18.5:
    print(f"{nome_usuario}, seu IMC é {imc: .2f} → Abaixo do peso")
if imc >= 18.5 and imc <= 24.9:
    print(f"{nome_usuario}, seu IMC é {imc: .2f}→ Peso normal")
if imc > 24.9:
    print(f"{nome_usuario}, seu IMC é {imc: .2f} → Acima do peso")

