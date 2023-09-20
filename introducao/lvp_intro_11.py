"""
Faça um programa que leia o raio de uma circunferência, calcule e apresente a área da mesma. Considere o valor de pi como 3.14159
"""
# Função principal
def main():
  # Variaveis
  raio = float()

  # Entrada de dados
  raio = float(input())
  
  # Processamento
  raio = 3.14159 * (raio ** 2)
  
  # Saida de dados
  print(raio)

  return 0

if __name__ == "__main__":
  main()
