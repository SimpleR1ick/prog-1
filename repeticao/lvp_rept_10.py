
"""
Faça um Algoritmo que leia 5 valores e escreva no final a 
soma dos valores positivos e a
média dos negativos. 
"""

# Função principal
def main():
    # Variaveis
    soma_pos = int(0)
    soma_neg = int(0)
    cont_neg = int(0)

    # Entrada de dados
    for _ in range(0, 5):
        num = int(input())

        # Procesamento
        if num < 0:
            soma_pos += num
        else:
            soma_neg += num
            cont_neg += 1

    # Saida de dados
    print(soma_pos)
    print(soma_neg / cont_neg)

    return 0

if __name__ == "__main__":
    main()