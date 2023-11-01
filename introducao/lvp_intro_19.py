# Solicita o valor da hora de trabalho e o número de horas trabalhadas no mês
valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcula os descontos
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

# Calcula o salário líquido
salario_liquido = salario_bruto - (ir + inss + sindicato)

# Exibe os resultados
print("+ Salário Bruto: R$", salario_bruto)
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido: R$", salario_liquido)
