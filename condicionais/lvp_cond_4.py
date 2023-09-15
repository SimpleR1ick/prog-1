"""
Ler quatro valores referentes a quatro notas escolares (0 a 100) 
de um aluno e escrever uma mensagem dizendo que o aluno foi aprovado, 
se o valor da média escolar for maior ou igual a 60.
"""


# Função principal
def main():
    # Variaveis
    media = float()

    # Entrada de dados
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())

    # Procesamento
    media = (n1 + n2 + n3 + n4) / 4

    # Saida de dados
    if media >= 60:
        print("APROVADO")

    return 0

if __name__ == "__main__":
    main()