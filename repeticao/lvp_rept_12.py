"""
Faça um Programa que leia números até que o usuário não queira 
mais digitar os números. No final escrever a soma dos valores 
positivos e a média dos valores negativos.  
(o usuário digitará a letra s para continuar 
informando dados e n quando quiser parar)
"""


# Função principal
def main():
    # Variaveis
    soma_positivos = 0
    soma_negativos = 0
    count_negativos = 0

    # Entrada de dados
    ler = input()

    while ler.lower() != 'n':
        numero = int(input())

        # Processamento 1
        if numero > 0:
            soma_positivos += numero
        elif numero < 0:
            soma_negativos += numero
            count_negativos += 1

        ler = input()

    # Processamento 2
    if count_negativos == 0:
        media_negativos = 0
    else:
        media_negativos = int(soma_negativos / count_negativos)

    # Saida de dados
    print(f'{soma_positivos} {media_negativos}')

    return 0

if __name__ == "__main__":
    main()