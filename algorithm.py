from queue import PriorityQueue
import pygame

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw, start):
    while current in came_from and current != start:
        current = came_from[current]
        if current != start:
            current.make_path()
        draw()
        yield  # Yield during path drawing too (optional, looks cooler)

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Stop everything if the window closes

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            end.make_end()
            yield from reconstruct_path(came_from, end, draw, start)
            return  # Done

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

        yield  # Let the main loop update the UI before continuing

    return  # No path found
