def encontrar_quadrado_perfeito_mais_proximo(a):
    x = 0
    while x * x <= a:
        x += 1
    x -= 1
    return x * x


def calcular_raiz_newton(a):
    x2 = encontrar_quadrado_perfeito_mais_proximo(a)
    x = x2
    for _ in range(10):
        x = 0.5 * (x + a / x)
    return x


def main():
    while True:
        n = float(input())
        if n < 0:
            break

        raiz_aproximada = calcular_raiz_newton(n)
        print(f"N={n:.4f} RAIZ={raiz_aproximada:.6f}")


if __name__ == "__main__":
    main()
