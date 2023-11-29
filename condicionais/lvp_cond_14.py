"""
Escreva um algoritmo que leia o número de litros vendidos e o 
tipo de combustível (codificado da seguinte forma: 
A-álcool ou  G-gasolina), calcule e imprima o valor a ser 
pago pelo cliente sabendo-se que o preço do litro da 
gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90
"""


# Função principal
def main():
    # Variaveis
    litros = total = desconto = float()
    tipo = str()

    # Entrada de dados
    litros = float(input())
    tipo = input().upper()

    # Procesamento
    if tipo == 'A':
        # Preco do litro do Alcool
        total = litros * 2.90

        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05

    else:
        # Preco do litro Gasolina
        total = litros * 3.30
        
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06

    # Saida de dados
    total = total - (total * desconto)

    print(f"{total:.2f}")
    

    return 0

if __name__ == "__main__":
    main()

