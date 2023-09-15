"""
Ler dois valores numéricos inteiros e apresentar o resultado 
da diferença do maior pelo menor valor.
"""


# Função principal
def main():
    # Variaveis
    num1 = num2 = int()

    # Entrada de dados
    num1 = int(input())
    num2 = int(input())

    # Saida de dados
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)


    return 0

if __name__ == "__main__":
    main()