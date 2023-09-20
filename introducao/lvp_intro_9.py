# Função principal
def main():
    # Entrada de dados
    numero_carros = int(input())
    valor_vendas = float(input())
    salario_fixo = float(input())
    valor_por_carro = float(input())
    
    # Cálculo do salário final
    comissao_carro = numero_carros * valor_por_carro
    comissao_vendas = valor_vendas * 0.05
    salario_final = salario_fixo + comissao_carro + comissao_vendas
    
    # Saída de dados
    print(salario_final)

if __name__ == "__main__":
    main()
