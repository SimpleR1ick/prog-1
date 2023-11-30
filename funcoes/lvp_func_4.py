"""
Faça uma função que informe a quantidade de dígitos de um determinado 
número inteiro informado, UTILIZANDO DIV E MOD. SEM USAR RECURSO DE STRING
"""
from functions import contar_digitos

# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Procesamento
    digitos = contar_digitos(num)

    # Saida de dados
    print(digitos)

    return 0

if __name__ == "__main__":
    main()