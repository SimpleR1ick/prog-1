"""
Faça um programa que leia um valor inteiro de 100 a 999 (inclusive) e, 
utilizando recursos que já aprendemos em sala de aula, inverta esse número,
entregando um valor inteiro de três casas decimais 
(PROIBIDO UTILIZAR QUALQUER RECURSO DE STRING). 
Ao final, o programa deverá verificar se o valor digitado é uma CAPICUA.
"""


# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Procesamento
    c = num // 100
    d = (num % 100) // 10
    u = num % 10

    # Calcula o número invertido
    invertido = u * 100 + d * 10 + c

    # Saida de dados
    if invertido == num:
        print('É UMA CAPICUA')
    else:
        print('NÃO É UMA CAPICUA')

    return 0

if __name__ == "__main__":
    main()