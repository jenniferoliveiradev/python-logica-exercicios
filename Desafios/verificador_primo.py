numero = int(input("Digite um numero: "))
primo = True

for i in range (2, numero):
    if numero % i == 0:
        primo = False

if primo == True:
    print(f" {numero} é primo")
else:
    print(f" {numero} Não é primo")