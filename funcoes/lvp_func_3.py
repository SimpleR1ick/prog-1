"""
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere 'P', se seu argumento for positivo, 
e 'N', se seu argumento  negativo ou 'Z' se for zero.
"""
from functions import positivo_negativo

# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Procesamento
    result = positivo_negativo(num)

    # Saida de dados
    print(result)

    return 0

if __name__ == "__main__":
    main()