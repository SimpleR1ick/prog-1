"""
"""


# Função principal
def main():
    # Variaveis
    valor_hora = horas_trabalhadas = float()

    # Entrada de dados
    valor_hora = float(input())
    horas_trabalhadas = float(input())

    # Procesamento
    salario_bruto = valor_hora * horas_trabalhadas

    ir = 0.11 * salario_bruto
    inss = 0.08 * salario_bruto
    sindicato = 0.05 * salario_bruto

    salario_liquido = salario_bruto - (ir + inss + sindicato)

    # Saida de dados
    print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
    print(f"- IR (11%) : R$ {ir:.2f}")
    print(f"- INSS (8%) : R$ {inss:.2f}")
    print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
    print(f"= Salário Líquido : R$ {salario_liquido:.2f}")

    return 0

if __name__ == "__main__":
    main()
