"""
Tendo como dados de entrada a altura e o sexo (M ou F) de uma pessoa, 
calcule e mostre seu peso ideal, utilizando as seguintes fórmulas: 
para sexo masculino: peso ideal = (72.7 * altura) - 58
para sexo feminino: peso ideal = (62.1 * altura) - 44.7
"""


# Função principal
def main():
    # Variaveis
    sexo = str()
    altura = float()
    peso_ideal = float()

    # Entrada de dados
    sexo = input("Digite o sexo (M ou F): ")
    altura = float(input("Digite a altura (em metros): "))

    # Processamento
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7

    # Saida de dados
    print(f"{peso_ideal:.3f}")

    return 0


if __name__ == "__main__":
    main()
