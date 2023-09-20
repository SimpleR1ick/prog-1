# Função principal
def main():
    # Variaveis
    custo_total = int(0)

    # Entrada de dados
    custo_fabrica = int(input())

    # Processamento
    lucro_d = custo_fabrica * 0.28
    imposto = custo_fabrica * 0.45

    custo_total = custo_fabrica + (lucro_d + imposto)

    # Saida de dados
    print(custo_total)

    return 0

if __name__ == "__main__":
    main()