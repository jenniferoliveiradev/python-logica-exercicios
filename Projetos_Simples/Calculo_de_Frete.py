print("0 ou 1 → São Paulo → R$ 15,00, \n2 ou 3 → Rio de Janeiro → R$ 20,00, \n4 ou 5 → Sul do Brasil → R$ 30,00, \n6 ou 7 → Nordeste → R$ 45,00, \n8 ou 9 → Norte/Centro-Oeste → R$ 60,00, \nPeso acima de 10kg → R$ 20,00 ")

cep_destino = input("Digite o primeiro dígito do seu CEP: ")

if cep_destino == "0" or cep_destino == "1":
    peso_encomenda = float(input("Digite o peso do pacote: "))
    frete = 15
    if peso_encomenda > 10:
        frete += 20  
    print(f"Frete: R$ {frete: .2f}")

elif cep_destino == "2" or cep_destino == "3":
    peso_encomenda = float(input("Digite o peso do pacote: "))
    frete = 20  
    if peso_encomenda > 10:
        frete += 20  
    print(f"Frete: R$ {frete: .2f}")

elif cep_destino == "4" or cep_destino == "5":
    peso_encomenda = float(input("Digite o peso do pacote: "))
    frete = 30
    if peso_encomenda > 10:
        frete += 20 
    print(f"Frete: R$ {frete: .2f}")

elif cep_destino == "6" or cep_destino == "7":
    peso_encomenda = float(input("Digite o peso do pacote: "))
    frete = 45
    if peso_encomenda > 10:
        frete += 20 
    print(f"Frete: R$ {frete: .2f}")

elif cep_destino == "8" or cep_destino == "9":
    peso_encomenda = float(input("Digite o peso do pacote: "))
    frete = 60
    if peso_encomenda > 10:
        frete += 20 
    print(f"Frete: R$ {frete: .2f}")

else: 
    print("CEP inválido")