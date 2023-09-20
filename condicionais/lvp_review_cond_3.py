"""
Tendo como dados de entrada os sexo, o peso e a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

- para homens: (72.7 * h) – 58
- para mulheres: (62.1 * h) – 44.7

E que calcule seu IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC o peso dividido pelo quadrado da altura

A condição do indivíduo segue a classificação da tabela abaixo:
IMC 	Classificação
Abaixo de 17 	MUITO ABAIXO DO PESO
Entre 17 e 18,49 	ABAIXO DO PESO
Entre 18,50 e 24,99 	PESO NORMAL
Entre 25 e 29,99 	ACIMA DO PESO
Entre 30 e 34,99 	OBESIDADE I
Maior que 34,99 	OBESIDADE II (SEVERA)
"""


# Função principal
def main():
    # Variaveis
    sexo = str()
    peso = altura = float()

    # Entrada de dados
    sexo = input().upper()
    peso = float(input())
    altura = float(input())

    # Procesamento
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    else:
        peso_ideal = (62.1 * altura) - 44.7

    # Calculando o IMC
    imc = peso / (altura ** 2)

    # Calculando classificação
    if imc < 17:
        classificacao = 'MUITO ABAIXO DO PESO'
    elif 17 <= imc < 18.5:
        classificacao = 'ABAIXO DO PESO'
    elif 18.5 <= imc < 25:
        classificacao = 'PESO NORMAL'
    elif 25 <= imc < 30:
        classificacao = 'ACIMA DO PESO'
    elif 30 <= imc < 35:
        classificacao = 'OBESIDADE I'
    else:
        classificacao = 'OBESIDADE II (SEVERA)'

    # Saida de dados
    print(f"PESO IDEAL: {peso_ideal:.2f}")
    print(f"IMC: {imc:.2f}")
    print(classificacao)

    return 0

if __name__ == "__main__":
    main()