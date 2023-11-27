"""
Faça um programa que leia 2 strings e informe se as duas strings possuem 
o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""


# Função principal
def main():
    # Variaveis
    string1 = string2 = str()
    
    # Entrada de dados
    string1 = input()
    string2 = input()

    # Saida de dados
    if len(string1) == len(string2):
        print("MESMO TAMANHO")
    else:
        print("TAMANHO DIFERENTE")

    if string1 == string2:
        print("CONTEÚDO IGUAL")
    else:
        print("CONTEÚDO DIFERENTE")

    return 0


if __name__ == "__main__":
    main()
