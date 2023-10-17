"""
Faça um Algoritmo que leia 5 valores inteiros e 
escreva no final a média dos valores lidos.
"""


# Função principal
def main():
    # Variaveis
    media = int(0)
    cont = int(0)

    # Entrada de dados
    while cont < 5:
        media += int(input())
        cont += 1

    # Saida de dados
    print(media / cont)

    return 0

if __name__ == "__main__":
    main()