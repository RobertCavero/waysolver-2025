import random

# Solicita as coordenadas dos pontos ao usuário
def obter_coordenadas():
    print("Digite as coordenadas do ponto de partida (pp):")
    pp_x = float(input("x: "))
    pp_y = float(input("y: "))
    
    print("Digite as coordenadas do ponto de destino (pd):")
    pd_x = float(input("x: "))
    pd_y = float(input("y: "))
    
    n = int(input("Digite a quantidade de pontos a serem gerados (n): "))
    
    return (pp_x, pp_y), (pd_x, pd_y), n

# Gera coordenadas com base nos requisitos
def gerar_pontos(pp, pd, n):
    # Calcula ci e cf (1.1 vezes as coordenadas)
    ci = (pp[0] * 1.1, pp[1] * 1.1)
    cf = (pd[0] * 1.1, pd[1] * 1.1)
    
    # Calcula quantidade de pontos caminho (pc) e obstáculos (po)
    n_pc = int(0.8 * n)  # 80% dos pontos
    n_po = int(0.2 * n)  # 20% dos pontos
    
    # Define limites para geração aleatória baseado nos pontos extremos
    min_x = min(pp[0], pd[0], ci[0], cf[0])
    max_x = max(pp[0], pd[0], ci[0], cf[0])
    min_y = min(pp[1], pd[1], ci[1], cf[1])
    max_y = max(pp[1], pd[1], ci[1], cf[1])
    
    # Gera pontos caminho (pc)
    pontos_caminho = []
    for _ in range(n_pc):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        pontos_caminho.append((x, y, "pc"))
    
    # Gera pontos obstáculo (po)
    pontos_obstaculo = []
    for _ in range(n_po):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        pontos_obstaculo.append((x, y, "po"))
    
    # Cria matriz com todos os pontos
    matriz_pontos = [
        (pp[0], pp[1], "pp"),
        (pd[0], pd[1], "pd"),
        (ci[0], ci[1], "ci"),
        (cf[0], cf[1], "cf")
    ] + pontos_caminho + pontos_obstaculo
    
    return matriz_pontos

# Função principal
def main():
    # Obtém os dados do usuário
    ponto_partida, ponto_destino, quantidade = obter_coordenadas()
    
    # Gera todos os pontos
    matriz = gerar_pontos(ponto_partida, ponto_destino, quantidade)
    
    # Exibe a matriz resultante
    print("\nMatriz de pontos gerada:")
    print("x\t\ty\t\tclassificação")
    print("-" * 40)
    for ponto in matriz:
        print(f"{ponto[0]:.2f}\t\t{ponto[1]:.2f}\t\t{ponto[2]}")

# Executa o programa
if __name__ == "__main__":
    main()