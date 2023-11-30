"""
Faça um programa, em Python 3.x, que leia a massa (Kg) e a força 
(em Newtons), submetidas sobre um corpo.  e informe qual é a 
aceleração que ele adquire;
"""


# Função principal
def main():
    # Variaveis
    massa = forca = float()

    # Entrada de dados
    massa = float(input())
    forca = float(input())

    # Procesamento
    aceleracao = forca / massa

    # Saida de dados
    print(aceleracao)

    return 0

if __name__ == "__main__":
    main()