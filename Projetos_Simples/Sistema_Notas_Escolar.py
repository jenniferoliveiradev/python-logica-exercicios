matriz = []
alunos = 0
media_alunos = 0
nomes = []
qtd_alunos = int(input("Quantos alunos tem na turma? "))
qtd_materias = int(input("Quantas matérias tem? "))

for i in range(qtd_alunos):
    aluno = []
    nome_aluno = input("Qual o nome do aluno: ")
    for j in range(qtd_materias):
        nota_aluno = float(input("Digite a nota: "))
        aluno.append(nota_aluno)
    matriz.append(aluno)
    nomes.append(nome_aluno)

maior_media = -1
menor_media = 11
aluno_maior_media = ""
aluno_menor_media = ""
media_aluno = []

for i in range(len(matriz)):
    soma = 0
    
    for j in range(len(matriz[i])):
        elemento = matriz[i][j]
        soma += elemento
    media = soma / qtd_materias
    if media > maior_media:
        maior_media = media  
        aluno_maior_media = nomes[i]
    if media < menor_media:
        menor_media = media
        aluno_menor_media = nomes[i]
    media_aluno.append(media)

    if media >= 6:
        print(f"{nomes[i]} esta aprovado(a)!")
    else:
        print(f"{nomes[i]} esta reprovado(a)!")

media_geral = sum(media_aluno) / qtd_alunos

for i in range(len(nomes)):
    print(f"A média do(a) {nomes[i]} é: {media_aluno[i]:.2f}")
print(f"A maior média: {maior_media:.2f}! e o dono(a) da maior média é: {aluno_maior_media}")
print(f"A menor média: {menor_media:.2f}! e o dono(a) da menor média é: {aluno_menor_media}")
print(f"A média geral é: {media_geral:.2f}")