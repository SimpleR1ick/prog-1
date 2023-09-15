"""
Ler um valor inteiro e escrever se é positivo ou negativo 
(só para efeitos desse programa, considere o valor zero como positivo).
"""


# Função principal
def main():
    # Variaveis
    num = int()

    # Entrada de dados
    num = int(input())

    # Saida de dados
    if num >= 0:
        print("POSITIVO")
    else:
        print("NEGATIVO")
    
    return 0

if __name__ == "__main__":
    main()