"""
Faça um programa que peça o tamanho de um arquivo para download 
(em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo 
usando este link (em segundos).
"""


# Função principal
def main():
    """Função para calcular velocidade de download em relação ao 
    tamanho do arquivo.

    Returns:
        int: sucesso
    """
    # Variaveis
    tamanho = int()
    velocidade = int()
    tempo = int()

    # Entrada de dados
    tamanho = int(input())
    velocidade = int(input())

    # Processamento
    velocidade /= 8
    tempo = tamanho / velocidade

    # Saida de dados
    print(f"{tempo} segundos")

    return 0


if __name__ == "__main__":
    main()
