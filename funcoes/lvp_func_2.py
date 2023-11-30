"""
Faça um programa que leia tres número e, a partir de uma função, 
informe o resultado da soma, dos mesmos.
"""
from functions import somar_numeros

# Função principal
def main():
    # Variaveis
    num1 = num2 = int()

    # Entrada de dados
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    # Processamento
    result = somar_numeros(num1, num2)

    # Saida de dados
    print(somar_numeros(result, num3))

    return 0

if __name__ == "__main__":
    main()