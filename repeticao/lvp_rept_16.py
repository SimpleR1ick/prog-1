def main():
    # Variaveis
    idade = int(0)
    soma = int(0)
    lendo = bool(True)
    i = int(0)
    
    # Entrada de dados
    while lendo:
        idade = int(input())
        
        if idade == 0:
            lendo = False
        else:
            # Processamento
            soma += idade
            i += 1
    
    # Saida de dados
    print(soma / i)
    
if __name__ == "__main__":
    main()