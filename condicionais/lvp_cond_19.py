"""
Faça um algoritmo para ler: quantidade atual em estoque, quantidade 
máxima em estoque e quantidade mínima em estoque de um produto. 
Calcular e escrever a quantidade média 
((quantidade média = quantidade máxima + quantidade mínima)/2). 
Se a quantidade em estoque for maior ou igual a quantidade média 
escrever a mensagem 'NÃO EFETUAR COMPRA', 
senão escrever a mensagem 'EFETUAR COMPRA'.
"""


# Função principal
def main():
    # Variaveis
    atual, maxima, minima, media = int()

    # Entrada de dados
    atual = int(input())
    maxima = int(input())
    minima = int(input())

    # Procesamento
    media = (maxima + minima) / 2

    # Saida de dados
    if atual >= media:
        print("NÃO EFETUAR COMPRA")
    else:
        print('EFETUAR COMPRA')

    return 0

if __name__ == "__main__":
    main()