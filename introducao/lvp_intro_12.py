"""
Faça um programa que receba um número inteiro de 3 dígitos e apresente esse número ao contrário. Ex: 123 >> 321  ;  981 >> 189
"""


# Função principal
def main():
  # Variaveis

  # Entrada de dados
  num = int(input())

  # Processamento
  c = num // 100
  d = (num // 10) % 10
  u = num % 10

  # Saida de dados
  print(f'{u}{d}{c}')

  return 0


if __name__ == "__main__":
  main()
