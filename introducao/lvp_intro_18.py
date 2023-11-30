"""
Faça um programa, em Python 3.x, que receba dois números inteiros, 
um em uma variável a e outro em uma variável b. 

Proceda a troca dos valores das variáveis, de forma que o valor de b 
passe pra a e vice-versa. Apresente o valor das variáveis a e b, 
depois da troca.
"""


# Função principal
def main():
    # Variaveis
    temp = int()

    # Entrada de dados
    a = int(input())
    b = int(input())

    # Procesamento
    temp = b
    b = a
    a = temp

    # Saida de dados
    print(f"{a} e {b}")

    return 0

if __name__ == "__main__":
    main()