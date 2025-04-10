import random

# Solicita as coordenadas dos pontos ao usuário
def obter_coordenadas():
    print("Digite as coordenadas (numeros inteiros) do ponto de partida (pp):")
    pp_x = int(input("x: "))
    pp_y = int(input("y: "))
    
    print("Digite as coordenadas (numeros inteiros) do ponto de destino (pd):")
    pd_x = int(input("x: "))
    pd_y = int(input("y: "))
    
    n = int(input("Digite a quantidade de pontos (numeros inteiros) a serem gerados (n): "))
    
    return (pp_x, pp_y), (pd_x, pd_y), n

# Gera coordenadas com base nos requisitos
def gerar_pontos(pp, pd, n):
    # Calcula ci (0.1 vezes as coordenadas de pp) e cf (1.1 vezes as coordenadas de pd)
    ci = (int(pp[0] * 0.1), int(pp[1] * 0.1))
    cf = (int(pd[0] * 1.1), int(pd[1] * 1.1))
    
    # Calcula quantidade de pontos caminho (pc) e obstáculos (po) com inteiros
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
        x = random.randint(min_x,max_x)
        y = random.randint(min_y,max_y)
        pontos_caminho.append((x, y, "pc"))
    
    # Gera pontos obstáculo (po)
    pontos_obstaculo = []
    for _ in range(n_po):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
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
        print(f"{ponto[0]}\t\t{ponto[1]}\t\t{ponto[2]}")

# Executa o programa
if __name__ == "__main__":
    main()