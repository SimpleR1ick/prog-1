# Função principal
def main():
    # Variaveis
    peso = int()
    idade = int()
    ingerir = float()
    total = float()

    # Entrada de dados
    idade = int(input())
    peso = float(input())

    # Processamento
    if idade <= 17:
        ingerir = 0.040
    elif idade <= 55:
        ingerir = 0.035
    elif idade <= 65:
        ingerir = 0.030
    else:
        ingerir = 0.025
    
    total = peso * ingerir

    # Saida de dado
    print(f"{total:.1f} LITROS")


if __name__ == "__main__":
    main()
