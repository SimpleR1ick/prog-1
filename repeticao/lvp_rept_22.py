"""
Um jogo de videogame gera um relatório após processar os dados de um 
campeonato. 

Neste campeonato vários jogadores participam de 10 fases, onde os pontos 
são contabilizados por tipos de erros e tipos de acertos para cada fase. 

Os acertos são caracterizados pelas strings: A1, A2 e A3. 
Já os erros são  caracterizados pelas strings: E1, E2, E3.


A1 – soma 5 pontos
A2 – soma 7 pontos
A3 – soma 10 pontos
E1 – subtrai 2 pontos, se tiver pontos>0
E2 – subtrai 5 pontos, se tiver pontos>0
E3 – zera a pontuação

Os dados são fornecidos nesta ordem:
Nick name do jogador
Tipo de erro/acerto para cada uma das 10 fases.
Considere que os dados encerram quando um nick name igual a string vazia for fornecido para o
jogador.

Seu programa deverá calcular, para cada jogador, a pontuação ao final das 10 fases, sendo que toda
vez que a pontuação se tornar negativa deverá ser zerada. Imprima o nome do jogador e sua
pontuação final.

Ao final do campeonato imprima:
- A média de pontos do campeonato;
- O nome e a pontuação do jogador com maior pontuação;
"""


# Função principal
def main():
    # Inicialização de variáveis
    pontuacao_maxima = 0
    nome_max_pontuacao = ""
    total_pontos_campeonato = 0
    total_jogadores = 0

    # Loop para receber dados dos jogadores
    while True:
        # Recebe o nick name do jogador
        nome_jogador = input()
        
        # Verifica se deve encerrar o programa
        if nome_jogador == "":
            break

        # Inicializa a pontuação do jogador
        pontuacao_jogador = 0
        
        # Loop para processar os erros/acertos em cada fase
        for _ in range(10):
            tipo = input()

            # Calcula a pontuação com base no tipo de erro/acerto
            if tipo == "A1":
                pontuacao_jogador += 5
            elif tipo == "A2":
                pontuacao_jogador += 7
            elif tipo == "A3":
                pontuacao_jogador += 10
            elif tipo == "E1":
                pontuacao_jogador = max(0, pontuacao_jogador - 2)
            elif tipo == "E2":
                pontuacao_jogador = max(0, pontuacao_jogador - 5)
            elif tipo == "E3":
                pontuacao_jogador = 0

        # Atualiza as estatísticas do campeonato
        total_pontos_campeonato += pontuacao_jogador
        total_jogadores += 1

        # Atualiza a pontuação máxima e o nome do jogador com a pontuação máxima
        if pontuacao_jogador > pontuacao_maxima:
            pontuacao_maxima = pontuacao_jogador
            nome_max_pontuacao = nome_jogador

        # Imprime o nome do jogador e sua pontuação final
        print(f"{nome_jogador} {pontuacao_jogador} pontos")

    # Calcula a média de pontos do campeonato
    media_pontos_campeonato = total_pontos_campeonato / total_jogadores if total_jogadores > 0 else 0

    # Imprime as estatísticas finais do campeonato
    print(f"Média de Pontos = {media_pontos_campeonato:.2f} por jogo")
    print(f"Vencedor {nome_max_pontuacao} com {pontuacao_maxima} pontos")


    return 0

if __name__ == "__main__":
    main()

