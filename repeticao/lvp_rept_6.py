"""
Faça um Algoritmo que escreva na tela os números de 0 até 9.
"""


# Função principal
def main():
    # Saida de dados
    for i in range(0, 11):
        # Verifica se o número e par
        if i % 2 == 0:
            print(i)

    return 0

if __name__ == "__main__":
    main()