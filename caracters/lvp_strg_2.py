"""
Faça um programa que permita ao usuário digitar o seu nome e em seguida 
mostre o nome do usuário de trás para frente utilizando somente letras 
maiúsculas e, OBRIGATORIAMENTE, comando de repetição. 

Dica: lembre-se que ao informar o nome o usuário pode 
digitar letras maiúsculas ou minúsculas.
"""


# Função principal
def main():
    # Variaveis
    nome = str()
    invertido = str("")

    # Entrada de dados
    nome = input("Digite seu nome: ").upper()

    # Procesamento
    for letra in nome:
        invertido = letra + invertido

    # Saida de dados
    print(invertido)

    return 0

if __name__ == "__main__":
    main()
