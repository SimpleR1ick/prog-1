"""
MModifique o programa anterior (APNP LVP STRINGS 4)  
de modo que a escada seja invertida.
"""

# Função principal
def main():
    # Variaveis
    nome = str()

    # Entrada de dados
    nome = input().upper()

    # Saida de dados
    for i in range(len(nome), 0, -1):
        print(nome[:i])

    return 0

if __name__ == "__main__":
    main()