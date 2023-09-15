"""
"""


# Função principal
def main():
    # Variaveis
    a = b = c = int()

    # Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    # Saida de dados
    if a >= b + c or b >= a + c or c >= a + b:
        print("NÃO É TRIÂNGULO")

    elif a == b == c:
        print("EQUILÁTERO")

    elif a == b or a == c or b == c:
        print("ISÓSCELES")

    else:
        print("ESCALENO")

    return 0

if __name__ == "__main__":
    main()

