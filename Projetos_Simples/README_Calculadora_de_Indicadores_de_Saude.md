# Calculadora de Indicadores de Saúde

Programa em Python, executado no terminal, que recebe dados básicos do usuário (peso, altura, pressão arterial e glicemia) e gera um relatório com a classificação de cada indicador.

Projeto desenvolvido durante meus estudos de Python, para praticar **funções**, **condicionais** e **entrada e saída de dados**.

## O que o programa faz

- Calcula o **IMC** (Índice de Massa Corporal) e classifica o resultado.
- Classifica a **pressão arterial** a partir dos valores sistólico e diastólico.
- Classifica a **glicemia**, levando em conta se a medição foi feita **em jejum** ou não.
- Exibe um **relatório final** com o nome da pessoa e os três resultados.

## Faixas de classificação usadas

**IMC**

| IMC | Classificação |
|---|---|
| Abaixo de 18,5 | Abaixo do peso |
| De 18,5 a 24,9 | Peso normal |
| Acima de 24,9 | Acima do peso |

**Pressão arterial**

| Condição | Classificação |
|---|---|
| Sistólica ≥ 140 ou diastólica ≥ 90 | Hipertensão |
| Sistólica ≥ 120 ou diastólica ≥ 80 (e não se enquadra em hipertensão) | Pré-hipertensão |
| Abaixo disso | Normal |

**Glicemia em jejum**

| Glicemia | Classificação |
|---|---|
| Abaixo de 70 | Hipoglicemia |
| De 70 a 99 | Normal |
| De 100 a 125 | Pré-diabetes |
| Acima de 125 | Diabetes |

**Glicemia sem jejum**

| Glicemia | Classificação |
|---|---|
| Abaixo de 140 | Normal |
| De 140 a 199 | Pré-diabetes |
| 200 ou mais | Diabetes |

## Como executar

Você precisa ter o Python 3 instalado. No terminal, dentro da pasta do arquivo:

```
python Calculadora_de_Indicadores_de_Saude.py
```

O programa vai fazer as perguntas na tela e, no final, mostrar o relatório.

## Exemplo de uso

```
Qual o seu nome? Julia
Qual o seu peso? 67
Qual a sua altura? 1.65
Qual a sua pressão? 114
Pressão diastólica: 90
Quanto esta a sua Glicemia? 90
Está em jejum? (s/n): s
Julia, seu imc é: 24.61 e a classificação esta: Peso normal, sua pressão esta: Hipertensão, sua glicemia esta: Normal
```

## Conceitos praticados

- Criação e uso de funções com parâmetros e retorno
- Estruturas condicionais (`if`, `elif`, `else`) e operadores lógicos (`and`, `or`)
- Conversão de tipos (`float`) e leitura de dados com `input`
- Formatação de texto com f-strings
- Teste de valores de borda e correção de faixas de classificação

## Aviso

Este é um projeto de estudo. Os resultados são apenas uma classificação simples dos valores informados e **não substituem avaliação médica**.
