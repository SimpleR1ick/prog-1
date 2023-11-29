"""
Desenvolva um programa que receba, enquanto o usuário responder sim "s", 
dois valores para efetuar operações matemáticas de acordo com a opção do 
usuário, 
1 para soma, 
2 para subtração (do primeiro pelo segundo), 
3 para multiplicação, 
4 para divisão (do primeiro pelo segundo), 
5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice). Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.
"""


# Função principal
def main():
    # Variaveis
    num1 = num2 = float()
    resultado = float()
    operacao = str()
    calcular = str()

    # Entrada de dados
    calcular = input()

    # Procesamento
    while calcular.lower() == 's':
        # Solicitar a operação desejada
        operacao = input()

        # Solicitar dois valores ao usuário
        num1 = float(input())
        num2 = float(input())
        
        # Verificar a escolha do usuário e realizar a operação correspondente
        if operacao == '1':
            resultado = num1 + num2
            
        elif operacao == '2':
            resultado = num1 - num2
            
        elif operacao == '3':
            resultado = num1 * num2
            
        elif operacao == '4':
            resultado = num1 / num2  
           
        elif operacao == '5':
            resultado = num1 ** num2
         
        elif operacao == '6':     
            resultado = num1 ** (1 / num2)
    
        else:
            print("OPERACAO INVALIDA")

        # Saida de dados
        print(resultado)
        
        calcular = input()

    
    return 0

if __name__ == "__main__":
    main()

