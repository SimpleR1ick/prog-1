"""
faça um programa que verifique os números de 1 a 5000 (ambos incluídos),
identificando os que são quadrados perfeitos e capicuas (capicuas é aquilo que lido de trás para frente é a mesma coisa: 121, 1001, 4334 etc)

Utilize as seguintes funções externas criadas por você:

a) uma função que retorne o tamanho de um número 
b) um função que inverta um número
c) uma função que verifique se o número é um quadrado perfeito
d) um função que verifique se um número é uma capicua

os outputs devem seguir o seguinte modelo

X É CAPICUA E QUADRADO PERFEITO
OU
X 
OU
X É QUADRADO PERFEITO
"""
from functions import eh_capicua, eh_quadrado_perfeito


def main():
    # Procesamento
    for numero in range(1, 5001):
        quadrado = eh_quadrado_perfeito(numero)
        capicua = eh_capicua(numero)

        # Saida de dados
        if quadrado and capicua:
            print(f"{numero} É CAPICUA E QUADRADO PERFEITO")

        elif capicua:
            print(f"{numero} É CAPICUA")

        elif quadrado:
            print(f"{numero} É QUADRADO PERFEITO")

        

    return 0

if __name__ == "__main__":
    main()