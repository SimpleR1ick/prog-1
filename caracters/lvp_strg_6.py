"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do 
usuário e imprima a data com o nome do mês por extenso.
"""


# Função principal
def main():
    # Variaveis
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    # Entrada de dados
    data_nascimento = input()

    # Procesamento
    dia, mes, ano = map(int, data_nascimento.split('/'))

    # Saida de dados
    print(f"{dia} de {meses[mes-1]} de {ano}")

    return 0

if __name__ == "__main__":
    main()