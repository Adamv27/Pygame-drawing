import pygame

def draw_canvas(screen, colors):
    screen.fill(colors[0])
    pygame.draw.rect(screen, colors[5], (20, 20, 500, 500))

    index = 1 # skip light grey
    for row in range(2):
        for column in range(4):
            pygame.draw.rect(screen, colors[index], ((60 * column) + 20, (60 * row) + 530, 60, 60))
            index += 1


def fill_square(screen, color, column, row):
    pygame.draw.rect(screen, color, (20 + (5 *column), 20 + (5 * row), 5, 5))
    pygame.display.update()