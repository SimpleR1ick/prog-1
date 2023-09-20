"""
Faça um Algoritmo para ler um valor N e imprimir todos 
os valores inteiros entre 1
(inclusive) e N (inclusive). 
Considere que o N será sempre maior que ZERO.
UTILIZE O COMANDO WHILE.
"""


# Função principal
def main():
    # Variaveis
    i = int(1)
    
    # Entrada de dados
    num = int(input())

    # Saida de dados
    while i <= num:
        print(i)
        i += 1

    return 0

if __name__ == "__main__":
    main()