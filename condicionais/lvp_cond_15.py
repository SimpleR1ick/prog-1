"""
Ler a hora de início e a hora de fim de um jogo de Xadrez 
(considere apenas horas inteiras, sem os minutos), 
em formato 24h. Calcule a duração do jogo em horas, 
sabendo-se que o tempo máximo de duração do jogo é 
de 24 horas e que o jogo pode iniciar em um dia e 
terminar no dia seguinte.
"""

# Função principal
def main():
    # Entrada de dados
    inicio = int(input())
    fim = int(input())

    # Calcula a duração do jogo
    if fim > inicio:
        duracao = fim - inicio
    elif fim == inicio:
        duracao = 24
    else:
        duracao = (24 - inicio) + fim
    
    # Saida de dados
    print(duracao)

    return 0

if __name__ == "__main__":
    main()