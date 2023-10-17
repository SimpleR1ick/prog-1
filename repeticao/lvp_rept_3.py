"""
Faça um Programa que leia números até que o usuário não queira mais digitar
os números. No final escrever a soma dos valores lidos. 
(o usuário digitará a letra s para continuar informando
dados e n quando quiser parar)
"""


# Função principal
def main():
    # Variaveis
    lendo = True
    soma = float(0)

    # Entrada de dados
    while lendo:
        ler = input().lower()

        if ler != 's':
            lendo = False
        else:
            soma += float(input())

    # Saida de dados
    print(soma)

    return 0

if __name__ == "__main__":
    main()