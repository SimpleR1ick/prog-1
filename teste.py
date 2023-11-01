"""
Faça um Programa que leia números até que o usuário não queira mais digitar
os números. No final escrever a soma dos valores lidos. 
(o usuário digitará a letra s para continuar informando
dados e n quando quiser parar)
"""


# Função principal
def main():
    # Variaveis
    soma = float(0)

    ler = input.lower()

    # Entrada de dados
    while ler:
        soma += float(input())

        ler = input().lower()

    # Saida de dados
    print(soma)

    return 0

if __name__ == "__main__":
    main()