import pygame
import pygame_gui
from grid import Spot
from algorithm import algorithm
import random
import tkinter as tk
from tkinter import filedialog

GRID_SIZE = 600
UI_HEIGHT = 140
WINDOW_HEIGHT = GRID_SIZE + UI_HEIGHT
WINDOW_WIDTH = GRID_SIZE

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Spot(i, j, gap, rows))
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, (128, 128, 128), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, (128, 128, 128), (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill((255, 255, 255))
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = min(max(y // gap, 0), rows - 1)
    col = min(max(x // gap, 0), rows - 1)
    return row, col


def main():
    def escolher_arquivo_txt():
        root = tk.Tk()
        root.withdraw()  #oculta janela tkinter
        arquivo = filedialog.askopenfilename(
        title="Escolher arquivo de mapa",
        filetypes=[("Arquivos de Texto", "*.txt")]
        )
        return arquivo

    
    button_width = 150
    button_height = 40
    spacing_x = 20
    spacing_y = 20
    start_x = 10
    start_y = GRID_SIZE + 20

    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("WaySolver")

    manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    #Botões
    start_button = pygame_gui.elements.UIButton(
    pygame.Rect((start_x, start_y), (button_width, button_height)),
    'Iniciar', manager)

    reset_button = pygame_gui.elements.UIButton(
    pygame.Rect((start_x + (button_width + spacing_x), start_y), (button_width, button_height)),
    'Resetar', manager)

    draw_button = pygame_gui.elements.UIButton(
    pygame.Rect((start_x + 2 * (button_width + spacing_x), start_y), (button_width, button_height)),
    'Modo Obstáculo', manager)

    maze_button = pygame_gui.elements.UIButton(
    pygame.Rect((start_x, start_y + button_height + spacing_y), (button_width, button_height)),
    'Gerar Labirinto', manager)

    load_map_button = pygame_gui.elements.UIButton(
    pygame.Rect((start_x + (button_width + spacing_x), start_y + button_height + spacing_y), (button_width, button_height)),
    'Carregar Mapa', manager)

    



    ROWS = 30
    grid = make_grid(ROWS, GRID_SIZE)
    start = end = None
    obstacle_mode = False
    mouse_held = False
    algorithm_generator = None  

    run = True
    while run:
        time_delta = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] < GRID_SIZE:
                    row, col = get_clicked_pos(event.pos, ROWS, GRID_SIZE)
                    spot = grid[row][col]

                    if event.button == 1:
                        mouse_held = True
                        if obstacle_mode:
                            if spot != start and spot != end:
                                spot.make_barrier()
                        elif not start and spot != end:
                            start = spot
                            start.make_start()
                        elif not end and spot != start:
                            end = spot
                            end.make_end()
                    elif event.button == 3:
                        spot.reset()
                        if spot == start:
                            start = None
                        elif spot == end:
                            end = None

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_held = False

            if event.type == pygame.MOUSEMOTION and mouse_held and obstacle_mode:
                if event.pos[1] < GRID_SIZE:
                    row, col = get_clicked_pos(event.pos, ROWS, GRID_SIZE)
                    spot = grid[row][col]
                    if spot != start and spot != end:
                        spot.make_barrier()

            #Botões
            if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm_generator = algorithm(lambda: draw(win, grid, ROWS, GRID_SIZE), grid, start, end)

                elif event.ui_element == reset_button:
                    start = end = None
                    grid = make_grid(ROWS, GRID_SIZE)
                    algorithm_generator = None  # reseta algoritmo

                elif event.ui_element == draw_button:
                    obstacle_mode = not obstacle_mode
                    draw_button.set_text("Modo Normal" if obstacle_mode else "Modo Obstáculo")

                elif event.ui_element == maze_button:
                    if start and end:
                        for row in grid:
                            for spot in row:
                                if not spot.is_start() and not spot.is_end():
                                    spot.reset()
                                    gerar_labirinto(grid, start, end)
                
                elif event.ui_element == load_map_button:
                    caminho_arquivo = escolher_arquivo_txt()
                    if caminho_arquivo:
                        start = end = None
                        grid = make_grid(ROWS, GRID_SIZE)
                        start, end = carregar_mapa_de_arquivo(caminho_arquivo, grid)



            manager.process_events(event)

        draw(win, grid, ROWS, GRID_SIZE)
        manager.update(time_delta)
        manager.draw_ui(win)

        if algorithm_generator:
            try:
                next(algorithm_generator)
            except StopIteration:
                algorithm_generator = None

        pygame.display.update()

    pygame.quit()

def gerar_labirinto(grid, start, end):
    for row in grid:
        for spot in row:
            #gera labirinto apenas se o inicio e o fim estiverem definidos
            if (not spot.is_start()) and (not spot.is_end()):
                if random.random() < 0.3:
                    spot.make_barrier()
                else:
                    spot.reset()

def carregar_mapa_de_arquivo(nome_arquivo, grid):
    start = end = None
    with open(nome_arquivo, 'r') as f:
        linhas = [linha.strip().split() for linha in f.readlines()]

    for i, linha in enumerate(linhas):
        for j, char in enumerate(linha):
            if j < len(grid) and i < len(grid[j]):  #inverter i por j
                spot = grid[j][i]  #corrige espelhamento
                if char == 'S':
                    spot.make_start()
                    start = spot
                elif char == 'E':
                    spot.make_end()
                    end = spot
                elif char == 'X':
                    spot.make_barrier()
                else:
                    spot.reset()
    return start, end




if __name__ == "__main__":
    main()
