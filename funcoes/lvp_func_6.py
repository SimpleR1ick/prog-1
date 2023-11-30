"""
1) Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO 
SUAS PRÓPRIAS FUNÇÕES), para resolver o seguinte problema:

a) Definir uma função em Python 3 que calcule o valor do fatorial de um 
número N inteiro maior ou igual a zero. 
Esta função recebe como parâmetro o valor de N. 
Esta função retorna o valor do fatorial de N calculado.

b) Faça um programa principal que leia diversos números inteiros maiores 
ou iguais a zero. Para cada número N lido imprima uma saída 
EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo. 
A condição de parada da entrada de dados é ler um número N menor que zero.

c) Invocar o programa principal.
"""
from functions import calcular_fatorial

def main():
    # Variaveis
    num = int()
    fatorial = int()

    while True:
        # Entrada de dados
        num = int(input())
        
        if num < 0:
            break

        fatorial = calcular_fatorial(num)

        # Saida de dados
        print(f"Fatorial({num})={fatorial:.0f}")

if __name__ == "__main__":
    main()

