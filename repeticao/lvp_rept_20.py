def main():
    # Declaração de variáveis
    turma_maior_ausencia = None
    turma_menor_ausencia = None
    maior_ausencia = int(-1)
    menor_ausencia = int(101)
    turmas_acima_20 = int(0)
    
    # Entrada de dados
    N = int(input())
    
    # Processamento
    for _ in range(N):
        # Entrada de dados para cada turma
        identificacao_turma = input()
        num_alunos = int(input())
        ausentes = 0
    
        for _ in range(num_alunos):
            matricula = input()
            frequencia = input()
            
            if frequencia == "A":
                ausentes += 1
    
        # Cálculo da porcentagem de ausência
        porcentagem_ausencia = (ausentes / num_alunos) * 100
    
        # Saída de dados
        print(f"TURMA= {identificacao_turma} AUSENCIA= {porcentagem_ausencia:.2f} %")
    
        # Verifica maior e menor ausência
        if porcentagem_ausencia > maior_ausencia:
            turma_maior_ausencia = identificacao_turma
            maior_ausencia = porcentagem_ausencia
    
        if porcentagem_ausencia < menor_ausencia:
            turma_menor_ausencia = identificacao_turma
            menor_ausencia = porcentagem_ausencia
    
        # Verifica se a turma tem porcentagem de ausência superior a 20%
        if porcentagem_ausencia > 20:
            turmas_acima_20 += 1
            
    # Saída dos resultados finais
    print(f"TURMA COM MAIOR % DE AUSENCIA= {turma_maior_ausencia} AUSENCIA= {maior_ausencia:.2f}%")
    print(f"TURMA COM MENOR % DE AUSENCIA= {turma_menor_ausencia} AUSENCIA= {menor_ausencia:.2f}%")
    print(f"{turmas_acima_20} TURMAS COM % DE AUSENCIA SUPERIOR A 20%")
    
if __name__ == "__main__":
    main()
