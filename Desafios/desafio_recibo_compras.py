nome_cliente = input("Digite o seu nome: ")
nome_produto = input("Digite o nome do produto: ")
quantidade_produto = int(input("Digite a quantidade de produtos: "))
preco_produto = float(input("Digite o valor do produto:"))
desconto_produto = int(input("Digite a porcentagem de desconto do produto: "))

subtotal = quantidade_produto * preco_produto
valor_desconto = subtotal * desconto_produto / 100
total = subtotal - valor_desconto
print("===== Recibo =====")
print(f"Cliente: {nome_cliente}\nProduto:  {nome_produto}\nQuantidade: {quantidade_produto}\n Preço unitário: R$ {preco_produto}\n Subtotal: R$ {subtotal}\n Desconto: R$ {valor_desconto}\n Total: R$ {total}")
print("==================")