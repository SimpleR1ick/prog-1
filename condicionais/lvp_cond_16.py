"""
A jornada de trabalho semanal de um funcionário é de 40 horas. 
O funcionário que trabalhar mais de 40 horas receberá hora extra, 
cujo cálculo é o valor da hora regular com um acréscimo de 50%. 
Escreva um algoritmo que leia o número de horas trabalhadas em um mês, 
o salário por hora e escreva o salário total do funcionário, 
que deverá ser acrescido das horas extras, caso tenham sido 
trabalhadas (considere que o mês possua 4 semanas exatas, totalizando o 
esperado de 160h/mês).
"""


# Função principal
def main():
    # Variaveis
    jornada_semanal = int(40)  # horas por semana
    horas_extras = int(0)

    # Entrada de dados
    horas_trabalhadas = float(input())
    salario_por_hora = float(input())

    # Procesamento    
    jornada_mensal = jornada_semanal * 4  # horas por mês

    # Verificar se o funcionário trabalhou horas extras
    if horas_trabalhadas > jornada_mensal:
        horas_extras = horas_trabalhadas - jornada_mensal

    # Calcular o salário total, incluindo horas extras (se houver)
    salario_extra = horas_extras * salario_por_hora * 1.5
    salario_total = (jornada_mensal * salario_por_hora) + salario_extra

    # Saida de dados
    print(f"{salario_total:.2f}")

    return 0

if __name__ == "__main__":
    main()