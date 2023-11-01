"""
Tem-se um conjunto de dados contendo o sexo (masculino, faminino) e 
altura de 5 pessoas. Fazer um algoritimo que calcule e escreva.

- a maior e a menor altura do grupo
- a media de altura das mulheres,
- a quantidade de homens
"""


# Função principal
def main():
    # Variaveis
    maior_altura = menor_altura = None
    soma_altura_mulheres = int(0)
    quantidade_homens = int(0)

    # Entrada de dados
    for _ in range(5):
        altura = float(input())
        sexo = input().lower()

        # Verifique a maior e a menor altura.
        if maior_altura is None or altura > maior_altura:
            maior_altura = altura
        if menor_altura is None or altura < menor_altura:
            menor_altura = altura

        # Verifique o sexo e atualize os cálculos de acordo.
        if sexo == 'f':
            soma_altura_mulheres += altura
        elif sexo == 'm':
            quantidade_homens += 1

    # Procesamento
    media_altura_mulheres = soma_altura_mulheres / 5

    # Saida de dados
    print(maior_altura)
    print(menor_altura)
    print(media_altura_mulheres)
    print(quantidade_homens)

    return 0

if __name__ == "__main__":
    main()