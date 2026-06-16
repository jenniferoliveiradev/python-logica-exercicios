nome = input("Digite o seu nome: ")
moeda_origem = input("Digite a moeda de origem (Ex: Real, Euro): ")
moeda_destino = input("Digite a moeda de destino (ex: Dólar, Iene): ")
valor_moeda = float(input("Digite um valor da Moeda: "))
cotacao_moeda = float(input("Digite o valor da cotação da Moeda: "))

valor_convercao = valor_moeda/ cotacao_moeda 

print("===== CONVERSOR =====")
print(f"Olá, {nome}! \nValor em {moeda_origem}: {valor_moeda: .2f} \nCotação {moeda_destino}: {cotacao_moeda: .2f} \nValor da Moeda: {valor_convercao: .2f}")
print("=====================")