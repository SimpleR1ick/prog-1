"""
Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, 
calcular e escrever o valor correspondente em graus Celsius. 
Fórmula: c = (f-32)/1.8
"""

# Função principal
def main():
    """Função para ler um numero e exibir em fahrenheit
    """
    # Entrada de dados
    fahrenheit = float(input("Digite a temperatura: "))

    # Processamento 
    celcius = (fahrenheit - 32) / 1.8

    # Saida de dados
    print(f"{celcius:.2f}")

    return 0

if __name__ == "__main__":
    main()
