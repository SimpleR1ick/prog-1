"""
Ler 3 valores (considere que não serão informados valores iguais) 
e escrever a soma dos dois maiores valores.
"""


# Função principal
def main():
    # Variaveis
    n1 = n2 = n3 = int()

    # Entrada de dados
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    # Saida de dados
    if n1 > n2 and n1 > 3:
        if n2 > n3:
            print(n1 + n2)
        else:
            print(n1 + n3)

    elif n2 > n3:
        if n1 > n3:
            print(n2 + n1)
        else:
            print(n2 + n3)
    else:
        if n1 > n2:
            print(n1 + n3)
        else:
            print(n2 + n3)


    return 0

if __name__ == "__main__":
    main()