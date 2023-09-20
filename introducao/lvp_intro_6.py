# Função principal
def main():
    # Variaveis
    qtd_eleitores = int(0)
    votos_brancos = int(0)
    votos_nulos   = int(0)
    votos_validos = int(0)

    # Entrada de dados
    qtd_eleitores = int(input())
    votos_brancos = int(input())
    votos_nulos   = int(input())
    votos_validos = int(input())

    # Processamento
    votos_brancos = (votos_brancos / qtd_eleitores) * 100
    votos_nulos   = (votos_nulos   / qtd_eleitores) * 100
    votos_validos = (votos_validos / qtd_eleitores) * 100

    # Saida de dados
    print(f'BRANCOS={votos_brancos:.1f}%')
    print(f'NULOS={votos_nulos:.1f}%')
    print(f'VALIDOS={votos_validos:.1f}%')

    return 0

if __name__ == "__main__":
    main()