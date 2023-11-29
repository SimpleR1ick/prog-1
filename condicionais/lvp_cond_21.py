"""
Desenvolva um programa que receba dois valores para efetuar operações 
matemáticas de acordo com a opção do usuário, 

1 para soma, 
2 para subtração (do primeiro pelo segundo), 
3 para multiplicação, 
4 para divisão (do primeiro pelo segundo), 
5 para exponenciação (o segundo número será a potência), 
6 para  raiz (o primeiro número será o radicando e o segundo o índice). 

Qualquer valor diferente desse deve retornar uma mensagem de erro. 

Apresente o resultado da operação.
"""


# Função principal
def main():
    # Variaveis
    num1 = num2 = int()
    total = float()

    # Entrada de dados
    opcao = int(input())

    if not 1 <= opcao <= 6:
        print('OPERACAO INVALIDA')
    else:
        num1 = float(input())
        num2 = float(input())

        # Procesamento
        if opcao == 1:  # Soma
            total = num1 + num2

        elif opcao == 2:  # Subtração
            total = num1 - num2

        elif opcao == 3:  # Multiplicação
            total = num1 * num2

        elif opcao == 4:  # Divisão
            total = num1 / num2

        elif opcao == 5:  # Potência
            total = num1 ** num2

        elif opcao == 6:  # Raiz
            total = num1 ** (1 / num2)

        # Saida de dados
        print(total)

    return 0


if __name__ == "__main__":
    main()
