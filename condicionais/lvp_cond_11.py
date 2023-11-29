"""
Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o referido cálculo. Lembre-se de que a variável A deve ser diferente de zero.
"""


# Função principal
def main():
    # Variaveis
    a = b = c = int()

    # Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    # Procesamento
    delta = (b ** 2) - (4*a*c)
    """
    print(
        (delta > 0)*f'{(-b + (delta ** 0.5)) / (2*a)} {(-b - (delta ** 0.5)) / (2*a)}' or
        (delta == 0)* ((-b + (delta ** 0.5)) / (2*a)) or "Raiz não real"
    )
    """
    # Saida de dados
    if delta > 0:
        # Raiz quadrada de delta
        delta **= (1/2)

        # Calculando valores de x' e x''
        x1 = (-b + delta) / (2*a) 
        x2 = (-b - delta) / (2*a)

        print(f'{x1:.1f} {x2:.1f}')
    
    elif delta == 0:
        # Calculando raiz unica
        print(-b / (2*a))

    else:
        print("Não possui raiz")

    return 0

if __name__ == "__main__":
    main()