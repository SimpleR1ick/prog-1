"""
Faça um programa que leia um número inteiro e diga se ele é par ou ímpar.
"""


# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Saida de dados
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")

    return 0

if __name__ == "__main__":
    main()