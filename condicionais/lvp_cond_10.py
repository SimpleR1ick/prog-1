"""
Ler 3 valores inteiros (considere que não serão informados valores iguais) 
e escrevê-los em ordem crescente.
"""


# Função principal
def main():

    # Entrada de dados
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    # Processamento
    if num1 < num2 and num1 < num3:
        menor = num1

        if num2 < num3:
            medio = num2
            maior = num3
        else:
            medio = num3
            maior = num2

    elif num2 < num1 and num2 < num3:
        menor = num2

        if num1 < num3:
            medio = num1
            maior = num3
        else:
            medio = num3
            maior = num1
    else:
        menor = num3

        if num1 < num2:
            medio = num1
            maior = num2
        else:
            medio = num2
            maior = num1

    # Saida de dados
    print(menor, medio, maior)

    return 0

if __name__ == "__main__":
    main()