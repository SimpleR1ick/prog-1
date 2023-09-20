"""
Um veículo parte do repouso em movimento retilíneo e acelera com aceleração escalar. Faça um programa, em Python 3.x, que leia a aceleração e o tempo decorrido do movimento desse veículo e calcule a velocidade escalar e a distância percorrida (usando a fórmula de movimento uniformemente variado) por um veículo.
"""


# Função principal
def main():
  # Variaveis
  x1 = x2 = int()
  y1 = y2 = int()

  # Entrada de dados
  x1 = int(input())
  y1 = int(input())
  x2 = int(input())
  y2 = int(input())

  # Processamento
  dAB = ((x2 - x1)**2 + (y2 - y1)**2)**(1 / 2)

  # Saida de dados
  print(dAB)

  return 0


if __name__ == "__main__":
  main()
