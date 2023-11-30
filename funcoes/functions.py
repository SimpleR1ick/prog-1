def somar_numeros(numero1: int, numero2: int) -> int:
    """Função para somar dois numeros

    Args:
        n1 (int): numero inteiro
        n2 (int): numero inteiro

    Returns:
        A soma dos dois itens
    """
    return numero1 + numero2


def positivo_negativo(numero: int) -> str:
    """Função para verificar se um numero é
    positivo ou negativo

    Args:
        num (int): numero analisado

    Returns:
        str: Um caracter do tipo do número
    """
    if numero == 0:
        return 'Z'
    elif numero > 0:
        return 'P'
    else:
        return 'N'
        

def contar_digitos(numero: int) -> int:
    """Função para contar a quantidade de digitos
    de um numero inteiro, utilizando div e mod

    Args:
        num (int): numero inteiro

    Returns:
        int: quantidade de digitos
    """
    if numero == 0:
        return 1  # Se o número for zero, ele tem um dígito

    qtd_digitos = 0
    numero = abs(numero)  # Lidando com números negativos

    while numero > 0:
        numero = numero // 10
        qtd_digitos += 1

    return qtd_digitos


def inverter_numero(numero: int) -> int:
    """Função para inverter um número utilizando div e mob

    Args:
        numero (int): a ser invertido

    Returns:
        int: numero invertido
    """
    inverso = 0

    while numero > 0:
        digito = numero % 10
        inverso = (inverso * 10) + digito
        numero = numero // 10

    return inverso


def quadrado_mais_proximo_atual(quadrado_atual, numero):
    """_summary_

    Args:
        quadrado_atual (_type_): _description_
        numero (_type_): _description_

    Returns:
        _type_: _description_
    """
    if (numero - quadrado_atual ** 2 < (quadrado_atual + 1) ** 2 - numero):
        return quadrado_atual
    else:
        return quadrado_atual + 1


def encontrar_quadrado_perfeito_mais_proximo(numero):
    """_summary_

    Args:
        numero (_type_): _description_

    Returns:
        _type_: _description_
    """
    candidato = 1

    while (candidato ** 2 < numero):
        candidato = candidato + 1

    candidato = quadrado_mais_proximo_atual(candidato - 1, numero)

    return candidato ** 2


def calcular_aproximacao_raiz_newton(numero):
    """_summary_

    Args:
        numero (_type_): _description_

    Returns:
        _type_: _description_
    """
    quadrado_proximo = encontrar_quadrado_perfeito_mais_proximo(numero)
    raiz_proxima = quadrado_proximo ** (1 / 2)
    raiz_aproximada = (numero + quadrado_proximo) / (2 * raiz_proxima)

    return raiz_aproximada


# Função para calcular o fatorial de N
def calcular_fatorial(N):
    if N == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, N + 1):
            fatorial *= i
        return fatorial


def calcular_mdc(a, b, c):
    # Função para calcular o MDC entre três números inteiros positivos
    return mdc_entre_dois(mdc_entre_dois(a, b), c)


def mdc_entre_dois(x, y):
    # Função auxiliar para calcular o MDC entre dois números inteiros positivos
    while y:
        x, y = y, x % y
    return x


def decimal_para_binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    
    return binario


def decimal_para_hexadecimal(numero):
    if numero == 0:
        return '0'
    
    hexadecimal = ''
    while numero > 0:
        resto = numero % 16
        
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + resto - 10) + hexadecimal

        numero //= 16
    
    return hexadecimal


def eh_quadrado_perfeito(numero):
    raiz_quadrada = int(numero ** 0.5)

    return raiz_quadrada ** 2 == numero


def eh_capicua(numero):
    if len(str(numero)) == 1:
        return False

    return numero == inverter_numero(numero)



