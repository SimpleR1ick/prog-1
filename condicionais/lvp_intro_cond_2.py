"""
Corrija a identação do código para que a saída coincida com a solução dada:
"""

# Função principal
def main():
    # Variaveis
    a = 40
    b = 30
    c = 20
    d = 10

    # Saida de dados
    if c > a:
        if d > c:
            print("p")
        if c > b:
            print("a")
        else:
            print("o")
    if a < b:
        print("t")
    else:
        print("r")
        print("p")
    if b < c:
        print("o")
    else:
        print("p")
        if c > b:
            print("a")
        else:
            print("a")
        if a < b:
            print("c")
        else:
            print("t")
        if b < c:
            print("a")
        else:
            print("o")

    return 0

if __name__ == "__main__":
    main()