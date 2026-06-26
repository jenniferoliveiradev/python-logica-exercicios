print("Boas vindas!")

total = 0
novo_produto = "s"


while novo_produto == "s":
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    total += preco_produto
    
    novo_produto = input("Adicionar novo produto?")
    print(f"Total parcial: r$ {total:.2f}")
desconto = int(input("Digite o valor do desconto:"))
valor_desconto = total * desconto / 100
total_final = total - valor_desconto
print(f"===== RESUMO ===== \nTotal bruto: R$ {total:.2f} \nDesconto: R$ {valor_desconto:.2f} \nTotal final: R$ {total_final:.2f} \n==================")