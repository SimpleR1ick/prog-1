"""
Modifique o programa anterior (APNP LVP STRINGS 3) de forma a mostrar 
o nome em formato de escada.
"""

# Função principal
def main():
    # Variaveis
    nome = str()

    # Entrada de dados
    nome = input().upper()

    # Saida de dados
    for i in range(0, len(nome)+1):
        print(nome[:i])

    return 0

if __name__ == "__main__":
    main()