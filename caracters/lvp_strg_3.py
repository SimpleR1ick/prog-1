"""
Faça um programa que solicite o nome do usuário e imprima-o na vertical.
"""


# Função principal
def main():
    # Variaveis
    nome = str()

    # Entrada de dados
    nome = input().upper()

    # Saida de dados
    for letra in nome:
        print(letra)

    return 0

if __name__ == "__main__":
    main()