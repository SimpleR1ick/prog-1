"""
Faça um programa que, dados 4 números inteiros com entrada, 
apresenta a soma do maior e do menor valor.
"""


def main():
    # declaração de variáveis
    a = b = c = d = int()
    maior = int(0)
    menor = int(0)

    # Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # Procurando maior valor
    if a > b and a > c and a > d:
        maior = a
    elif b > c and b > d:
        maior = b
    elif c > d:
        maior = c
    else:
        maior = d

    # Procurando menor valor
    if a < b and a < c and a < d:
        menor = a
    elif b < c and b < d:
        menor = b
    elif c < d:
        menor = c
    else:
        menor = d

    # Saida de dados
    print(f'{maior + menor}')

    return 0


if __name__ == "__main__":
    main()
