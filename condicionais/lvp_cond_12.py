"""
Ler 3 valores (considere que não serão informados valores iguais) 
e escrever o maior deles.
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
    if n1 > n2 and n1 > n3:
        print(n1)

    elif n2 > n1 and n2 > n3:
        print(n2)
        
    else:
        print(n3)

    return 0

if __name__ == "__main__":
    main()