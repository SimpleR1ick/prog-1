"""
Elaborar um programa que efetue a leitura de um número inteiro 
e efetue a sua apresentação, caso o valor não seja divisível por três.
"""


# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Saida de dados
    if num % 3 != 0:
        print(num)

    return 0

if __name__ == "__main__":
    main()