"""
Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de 
uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre 
o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar 
este valor, calcular e escrever o seu salário total.
"""


# Função principal
def main():
    # Variaveis

    # Entrada de dados
    salario_fixo = float(input())
    valor_vendas = float(input())

    # Procesamento
    if valor_vendas > 1500:
        valor_extra = (valor_vendas - 1500) * 0.05
        valor_total = salario_fixo + (1500 * 0.03) + valor_extra
    else:
        valor_total = salario_fixo + (valor_vendas * 0.03)

    # Saida de dados
    print(valor_total)

    return 0

if __name__ == "__main__":
    main()
