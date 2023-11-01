"""
Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em
uma determinada cidade. Para isso, são fornecidos os seguintes dados:
- preço do kWh consumido;
- número do consumidor;
- quantidade de kWh consumidos durante o mês;
- código do tipo de consumidor (R-residencial, C-comercial, I-industrial).
O número do consumidor igual a zero deve ser usado como flag de parada. Fazer um algoritmo que:
- leia os dados descritos acima:
- calcule:
a) para cada consumidor, o total a pagar;
b) o maior consumo verificado;
c) o menor consumo verificado;
d) o total do consumo para cada um dos três tipos de consumidores;
e) a média geral de consumo;
- escreva:
a) para cada consumidor, o seu número e o total a pagar;
b) o que foi calculado nos itens b, c, d, e acima especificados.
"""


# Função principal
def main():
    # Variaveis
    maior_consumo = menor_consumo = None
    total_consumo_residencial = int(0)
    total_consumo_comercial = int(0)
    total_consumo_industrial = int(0)
    total_consumo_geral = int(0)
    quantidade_consumidor = int(0)
    registrando_consumo = bool(True)

    # Entrada de dados
    preco_kwh = float(input())

    while registrando_consumo:
        numero_consumidor = int(input())

        # Verifica se deve ler outro consumo
        if numero_consumidor == 0:
            registrando_consumo = False

        else:
            consumo_kwh = float(input())
            tipo_consumidor = input().upper()
            
            # Procesamento
            total_pagar = consumo_kwh * preco_kwh

            # Atualize os valores necessários.
            if maior_consumo is None or consumo_kwh > maior_consumo:
                maior_consumo = consumo_kwh

            if menor_consumo is None or consumo_kwh < menor_consumo:
                menor_consumo = consumo_kwh
            
            # Verifica consumo Residencial
            if tipo_consumidor == 'R':
                total_consumo_residencial += consumo_kwh
            # Verifica consumo Comercial
            elif tipo_consumidor == 'C':
                total_consumo_comercial += consumo_kwh
            # Verifica consumo Industrial
            elif tipo_consumidor == 'I':
                total_consumo_industrial += consumo_kwh

            # Soma o consumo ao total
            total_consumo_geral += consumo_kwh
            quantidade_consumidor += 1

            # Imprima os resultados para o consumidor atual.
            print(f"{numero_consumidor} {total_pagar}")

    # Calcule a média geral de consumo.
    media_consumo_geral = total_consumo_geral / quantidade_consumidor

    # Saida de dados
    print(maior_consumo)
    print(menor_consumo)
    print(total_consumo_residencial)
    print(total_consumo_comercial)
    print(total_consumo_industrial)
    print(media_consumo_geral)

    return 0

if __name__ == "__main__":
    main()


