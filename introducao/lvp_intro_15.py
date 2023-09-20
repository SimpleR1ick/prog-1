"""
Faça um programa que receba 4 (quatro) notas de um aluno (0 a 100) e apresente a sua média aritmética final.
"""


# Função principal
def main():
  # Variaveis
  n1 = n2 = n3 = n4 = int()

  # Entrada de dados
  n1 = float(input())
  n2 = float(input())
  n3 = float(input())
  n4 = float(input())

  # Processamento
  media = (n1 + n2 + n3 + n4) / 4

  # Saida de dados
  print(round(media, 2))

  return 0


if __name__ == "__main__":
  main()
