"""
Faça um programa que receba a idade de uma pessoa, em dias, e apresente a idade dessa pessoa em anos, meses e dias. Considere um ano com 365 dias e um MÊS com 30 dias.
"""


# Função principal
def main():
  # Variaveis
  anos = int()
  meses = int()
  dias = int()
  dias_finais = int()

  # Entrada de dados
  dias = int(input())

  # Processamento
  anos = dias // 365
  dias_restantes = dias % 365
  meses = dias_restantes // 30
  dias_finais = dias_restantes % 30

  # Saida de dados
  print(anos, meses, dias_finais)

  return 0


if __name__ == "__main__":
  main()
