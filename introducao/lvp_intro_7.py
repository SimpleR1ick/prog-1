# Função principal
def main():
    # Variaveis
    salario  = float(0)
    reajuste = int(0)

    # Entrada de dados
    salario  = float(input())
    reajuste = int(input())

    # Processamento
    salario += (salario * reajuste) / 100

    # Saida de dados
    print(int(salario))

    return 0

if __name__ == "__main__":
    main()