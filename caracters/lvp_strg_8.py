"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é 
idêntica se feita da direita para esquerda ou vice-versa. 

Por exemplo: OSSO e OVO são palíndromos. 

Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde 
os espaços foram ignorados. Faça um programa que leia uma seqüência 
de caracteres, mostre-a e diga se é um palíndromo ou não.
"""


# Função principal
def main():
    # Variaveis
    palavra = str("")
    inverte = str("")

    # Entrada de dados
    palavra = input().upper()

    # Procesamento
    palavra = palavra.replace(" ", "")
    inverte = palavra[::-1]

    # Saida de dados
    if palavra == inverte:
        print("É PALÍNDROMO")
    else:
        print("NÃO É PALÍNDROMO")

    return 0

if __name__ == "__main__":
    main()