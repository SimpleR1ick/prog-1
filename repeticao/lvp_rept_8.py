"""
Faça um Algoritmo que leia 5 valores inteiros e 
escreva no final a soma dos valores lidos.
"""


# Função principal
def main():
    # Variaveis
    soma = int(0)

    # Entrada de dados
    for _ in range(0, 5):
        soma += int(input())

    # Saida de dados
    print(soma)

    return 0

if __name__ == "__main__":
    main()