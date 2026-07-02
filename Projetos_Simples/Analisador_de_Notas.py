
quantidade = int(input("Quantos alunos tem na turma? "))
maior_nota = 0
menor_nota = 10
aprovados = 0 
reprovados = 0 
nome_maior = ""
nome_menor = ""
soma = 0

for i in range (quantidade):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    soma += nota

    if nota > maior_nota:
        maior_nota = nota
        nome_maior = nome

    if nota < menor_nota:
        menor_nota = nota
        nome_menor = nome


    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1
    

media = soma / quantidade
print(f"Média da turma: {media: .2f}")
print(f"Maior nota: {maior_nota} - {nome_maior}")
print(f"Menor nota: {menor_nota} - {nome_menor}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")



