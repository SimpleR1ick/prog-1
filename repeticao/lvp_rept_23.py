"""
Faça um programa em Python3 que leia o resultado uma rodada de um 
campeonato de futebol. O programa deve ler o nome do primeiro time 
e o nome do segundo time, em seguida a quantidade de gols primeiro time 
e a do segundo time (validação: aceite apenas valores maiores ou iguais 
a zero, caso ocorram entradas incorretas retorne à entrada dos dados). 

A condição de parada será informar o nome do primeiro time como string 
vazia (“”). Após a entrada de dados da partida o programa deverá 
imprimir o nome do time vencedor, ou imprimir que houve empate, ou 
imprimir que a quantidade de gols é inválida. 

Ao final da entrada de dados de todas as 
partidas da rodada o programa deve informar:

a) A média de gols da rodada
b) O time que fez mais gols em uma mesma partida da rodada
c) A quantidade de gols da partida em que houve o menor número de gols na rodada
"""


# Função principal
def main():
    # Inicialização de variáveis
    total_partidas = int(0)
    total_gols = int(0)
    time_mais_gols = str("")
    mais_gols_partida = int(0)
    menos_gols_partida = float()
    menos_gols = int()
    soma_gols_partida = int(0)
    media_gols = int(0)

    # Loop para receber dados das partidas
    while True:
        # Recebe o nome do primeiro time
        time1 = input()

        # Verifica se deve encerrar o programa
        if time1 == "":
            break

        # Recebe o nome do segundo time
        time2 = input()

        # Recebe a quantidade de gols do primeiro time
        gols_time1 = int(input())
        gols_time2 = int(input())

        # Atualiza estatísticas da rodada
        total_partidas += 1
        total_gols += gols_time1 + gols_time2

        # Verifica time vencedor ou empate
        if gols_time1 > gols_time2:
            vencedor = time1
        elif gols_time1 < gols_time2:
            vencedor = time2
        else:
            vencedor = None

        if not vencedor:
            print(f"{time1} x {time2}\nEmpate")
        else:
            print(f"{time1} x {time2}\nVencedor: {vencedor}")

        # Atualiza estatísticas para o time que fez mais gols em uma mesma partida
        if gols_time1 > mais_gols_partida:
            mais_gols_partida = gols_time1
            time_mais_gols = time1

        if gols_time2 > mais_gols_partida:
            mais_gols_partida = gols_time2
            time_mais_gols = time2

        # Atualiza estatísticas para a partida com menos gols
        soma_gols_partida = gols_time1 + gols_time2

        if soma_gols_partida < menos_gols_partida:
            menos_gols_partida = soma_gols_partida
            menos_gols = total_partidas

    # Calcula a média de gols da rodada
    if total_partidas > 0:
        media_gols = total_gols / total_partidas

    # Imprime as estatísticas finais da rodada
    print(f"Média de Gols: {media_gols:.2f} por jogo")
    print(f"Time que fez mais gols em um jogo: {time_mais_gols}")
    print(f"Menor número de gols em uma partida: {menos_gols}")

    return 0

if __name__ == "__main__":
    main()

