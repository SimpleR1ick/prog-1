"""
Faça um programa que leia dois números inteiros, 
a e b. Se a for maior que b, apresente a soma dos dois, 
caso a seja menor ou igual a b, apresente o resultado da 
multiplicação dos dois. 
"""


# Função principal
def main():
    # Variaveis
    a = b = int()
    
    # Entrada de dados
    a = int(input())
    b = int(input())

    # Saida de dados
    if a > b:
        print(a + b)
    else:
        print(a * b)

    return 0

if __name__ == "__main__":
    main()