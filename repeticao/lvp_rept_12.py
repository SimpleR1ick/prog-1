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
    lendo = bool(True)
    soma_pos = int(0)
    soma_neg = int(0)
    cont_neg = int(0)

    # Entrada de dados
    while lendo:
        ler = input().upper()

        # Verificando se deve continuar
        if ler != 's':
            lendo = False
        else:
            num = int(input())

            # Procesamento
            if num < 0:
                soma_pos += num
            else:
                soma_neg += num
                cont_neg += 1

    # Saida de dados
    print(f'{soma_neg / cont_neg} {soma_pos}')

    return 0

if __name__ == "__main__":
    main()