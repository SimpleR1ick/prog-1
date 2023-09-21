# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Procesamento
    m = (num // 1000) % 10
    c = (num // 100) % 10
    d = (num // 10) % 10
    u = num % 10

    # Calcula o número invertido
    invertido = u * 1000 + d * 100 + c * 10 + m

    # Saida de dados
    if invertido == num:
        print(f'{num} É UMA CAPICUA')
    else:
        print(f'{num} NÃO É UMA CAPICUA')

    return 0

if __name__ == "__main__":
    main()