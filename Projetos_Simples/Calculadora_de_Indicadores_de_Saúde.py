
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Peso normal"
    elif imc > 24.9: 
         return "Acima do peso"

def exibir_resultado(nome, imc, classificacao):
    print(f"{nome}, seu IMC é {imc:.2f} — {classificacao}")



def calcular_pressao(sistolica, diastolica):
    if sistolica < 120 and diastolica < 80:
        return  "Normal"
    elif sistolica >= 120 and sistolica <= 139 or diastolica >= 80 and diastolica <= 89:
        return"Pré-hipertensão"
    elif sistolica >= 140 or diastolica >= 90:
        return "Hipertensão"

def calcular_taxa_glicemia(glicemia, jejum):
    if jejum == True:
        if glicemia < 70:
            return "Hipoglicemia"
        elif glicemia >= 70 and glicemia <= 99:
            return "Normal"
        elif glicemia >= 100 and glicemia <= 125:
            return "Pré-diabetes"
        elif glicemia > 125:
            return "Diabetes"
    if jejum == False:
        if glicemia < 140:
            return "Normal"
        elif glicemia  >= 140 and glicemia <= 199:
            return "Pré-diabetes"
        elif glicemia < 200:
            return "Diabetes"
        
def exibir_relatorio(nome, imc, pressao, glicemia):
    print(f"{nome}, seu imc é: {imc:.2f}, sua pressão esta: {pressao}, sua glicemia esta: {glicemia}")

nome = input("Qual o seu nome? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
pressao_sistolica = float(input("Qual a sua pressão? "))
pressao_diastolica = float(input("Pressão diastólica: "))
glicemia = float(input("Quanto esta a sua Glicemia? "))
jejum = input("Está em jejum? (s/n): ") == "s"

imc = calcular_imc(peso, altura)
pressao = calcular_pressao(pressao_sistolica, pressao_diastolica)
glicemia_resultado = calcular_taxa_glicemia(glicemia, jejum)

exibir_relatorio(nome, imc, pressao, glicemia_resultado)



