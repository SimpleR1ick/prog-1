"""
Faça um programa que recebe n números inteiros maiores ou iguais a zero. 
Considere que a entrada de encerra quando um número menor que zero for 
informado pelo usuário.

- Faça uma função externa que receba um número inteiro maior ou igual a 
zero na base 10 e retorne um número inteiro maior ou igual a zero que 
representa, na base 2 (binário), o número na base 10 fornecido como 
entrada para esta função.

- Faça uma função externa que receba um número inteiro maior ou igual a 
zero na base 10 e retorne um número inteiro maior ou igual a zero que 
representa, na base 16 (hexadecimal), o número na base 10 fornecido 
como entrada para esta função.

- Para cada número LIDO imprima seu respectivo valor na base 2 e na 
base 16, conforme modelo abaixo. 
"""
from functions import decimal_para_binario, decimal_para_hexadecimal

def main():
    # Variaveis
    num = int()

    # Entrada de dados
    while True:
        num = int(input())
        
        if num < 0:
            break
        
        # Processamento
        binario = decimal_para_binario(num)
        hexadecimal = decimal_para_hexadecimal(num)
        
        # Saida de dados
        print(f"DEC={num} BIN={binario} HEX={hexadecimal}")

    return 0

if __name__ == "__main__":
    main()


