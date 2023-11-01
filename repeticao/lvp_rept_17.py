def main():
    # Variaveis
    s = int(0)
    
    # Processamento
    for i in range(1, 51):
        s += (2 * i - 1) / i
    
    # Saida de dados
    print(s)
    
if __name__ == "__main__":
    main()