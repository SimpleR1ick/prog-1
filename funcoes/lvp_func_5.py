"""
Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721. Usar, exclusivamente, DIV e MOD.
"""
from functions import inverter_numero

# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Procesamento
    invertido = inverter_numero(num)

    # Saida de dados
    print(invertido)

    return 0

if __name__ == "__main__":
    main()