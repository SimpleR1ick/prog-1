"""
Um veículo parte do repouso em movimento retilíneo e acelera com aceleração escalar. Faça um programa, em Python 3.x, que leia a aceleração e o tempo decorrido do movimento desse veículo e calcule a velocidade escalar e a distância percorrida (usando a fórmula de movimento uniformemente variado) por um veículo.
"""


# Função principal
def main():
  # Variaveis

  # Entrada de dados
  a = int(input())
  t = int(input())

  # Processamento
  v = float(a * t)
  d = float(0.5 * a * t**2)

  # Saida de dados
  print(f'{v} m/s {d} m')

  return 0


if __name__ == "__main__":
  main()
