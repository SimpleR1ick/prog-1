"""
Dado uma string com uma frase informada pelo usuário 
(incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""


# Função principal
def main():
    # Variaveis
    vogal_A = int(0)
    vogal_E = int(0)
    vogal_I = int(0)
    vogal_O = int(0)
    vogal_U = int(0)
    espacos = int(0)

    # Entrada de dados
    frase = input().upper()

    # Procesamento
    for char in frase:
        if char ==  ' ':
            espacos += 1
        elif char == 'A':
            vogal_A += 1
        elif char == 'E':
            vogal_E += 1
        elif char == 'I':
            vogal_I += 1
        elif char == 'O':
            vogal_O += 1
        elif char == 'U':
            vogal_U += 1

    # Saida de dados
    print(f"ESPAÇOS EM BRANCO = {espacos}")
    print(f"A = {vogal_A}")
    print(f"E = {vogal_E}")
    print(f"I = {vogal_I}")
    print(f"O = {vogal_O}")
    print(f"U = {vogal_U}")

    return 0

if __name__ == "__main__":
    main()