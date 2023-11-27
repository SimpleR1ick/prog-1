"""
Faça um programa que receba uma palavra e imprima cada letra em uma linha diferente.
"""


# Função principal
def main():
    # Variaveis
    palavra = str()

    # Entrada de dados
    palavra = input()

    # Procesamento
    for letra in palavra:
        # Saida de dados
        print(letra)

    return 0

if __name__ == "__main__":
    main()