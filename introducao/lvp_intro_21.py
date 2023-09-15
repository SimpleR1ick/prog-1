"""
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para 
cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;

"""
import math

# Função principal
def main():
    # Variaveis
    metros = int()
    tinta1 = tinta2 = int()
    cobertura = float()

    # Entrada de dados
    metros = int(input())

    # Procesamento
    cobertura = metros / 6

    tinta1 = math.ceil(cobertura / 18.0)
    tinta2 = math.ceil(cobertura / 3.6)

    # Saida de dados
    print(f"Você utilizará {tinta1} de 18L. Valor = {tinta1 * 80.0}")
    print(f"Você utilizará {tinta2} de 3,6L. Valor = {tinta2 * 25.0}")

    return 0

if __name__ == "__main__":
    main()