def main():
    # Variaveis
    s = int(0)

    # Processamento
    for i in range(1, 38):
        s += ((38 - i) * (39 - i)) / i
    
    # Saida de dados
    print(s)

if __name__ == "__main__":
    main()