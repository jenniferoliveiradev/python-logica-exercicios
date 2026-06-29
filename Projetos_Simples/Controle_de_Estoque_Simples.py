print("Boas Vindas!")

cadastro_produto = "s"
contador = 0
valor_total_estoque = 0
while cadastro_produto == "s":
    contador += 1
    nome_produto = input("Digite o nome do produto: ")
    quantidade_produto = int(input("Digite a quantidade em estoque: "))
    valor_unitario = float(input("Digite o valor da unidade: "))
    valor_total_estoque += quantidade_produto * valor_unitario
    print(f"{nome_produto} | quantidade: {quantidade_produto:} | valor total em estoque: {valor_total_estoque:.2f}")
    cadastro_produto = input("Deseja cadastrar outro produto? ")

print(f"===== ESTOQUE ===== \nTotal de produtos cadastrados: {contador} \nValor total do estoque: R$ {valor_total_estoque:.2f} ===================")