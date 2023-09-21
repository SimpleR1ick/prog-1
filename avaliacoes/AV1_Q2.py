def main():
    # Variaveis
    a = b = c = d = int()

    # Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # Procesamento
    if a > b and a > c and a > d:
        menores = b + c + d

    elif b > c and b > d:
        menores = a + c + d

    elif c > d:
        menores = a + b + d

    else:
        menores = a + b + c

    # Saida de dados
    print(menores)

    return 0

if __name__ == "__main__":
    main()