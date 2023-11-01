def main():
    # Variaveis
    s = int(0)
   
    # Processamento
    for i in range(1, 11):
        term = i / (i**2)
        
        if i % 2 == 0:
            s -= term
        else:
            s += term
    
    # Saida de dados
    print(s)
    
if __name__ == "__main__":
    main()