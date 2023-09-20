"""
Faça um Algoritmo para ler um valor inteiro e escrever a tabuada de 
1 a 10 do valor lido. 
"""


# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Saida de dados
    for i in range(1, 11):
        print(f"{i} x {num} = {i * num}")

    return 0

if __name__ == "__main__":
    main()