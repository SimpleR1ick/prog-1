"""
Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres 
(considere que as idades dos homens serão sempre diferentes entre si, 
bem como as das mulheres). Calcule e escreva a soma das idades do 
homem mais velho com a mulher mais nova, e o produto das idades do 
homem mais novo com a mulher mais velha.
"""


# Função principal
def main():
    # Variaveis
    idade_homem1 = idade_homem2 = int()
    idade_mulher1 = idade_mulher2 = int()

    # Entrada de dados
    idade_homem1 = int(input())
    idade_homem2 = int(input())
    idade_mulher1 = int(input())
    idade_mulher2 = int(input())

    # Processamento
    if idade_homem1 > idade_homem2:
        homem_mais_velho = idade_homem1
        homem_mais_novo = idade_homem2
    else:
        homem_mais_velho = idade_homem2
        homem_mais_novo = idade_homem1

    # Encontrar a mulher mais nova
    if idade_mulher1 < idade_mulher2:
        mulher_mais_nova = idade_mulher1
        mulher_mais_velha = idade_mulher2
    else:
        mulher_mais_nova = idade_mulher2
        mulher_mais_velha = idade_mulher1

    # Calcular a soma das idades do homem mais velho com a mulher mais nova
    soma_idades = homem_mais_velho + mulher_mais_nova

    # Calcular o produto das idades do homem mais novo com a mulher mais velha
    produto_idades = homem_mais_novo * mulher_mais_velha

    # Saida de dados
    print(soma_idades)
    print(produto_idades)

    return 0

if __name__ == "__main__":
    main()