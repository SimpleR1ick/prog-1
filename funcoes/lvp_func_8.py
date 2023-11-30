"""
"""
from functions import calcular_mdc

def main():
    # Variaveis
    n1 = n2 = n3 = int(0)

    for _ in range(4):
        # Entrada de dados
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())

        # Processamento
        resultado_mdc = calcular_mdc(n1, n2, n3)

        # Saida de dados
        print(f'MDC({n1}, {n2}, {n3})={resultado_mdc}')

# Invoca o programa principal
if __name__ == "__main__":
    main()
