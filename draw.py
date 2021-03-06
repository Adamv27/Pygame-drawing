import sys
import pygame


def draw_canvas(screen, colors):
    screen.fill(colors[0])
    pygame.draw.rect(screen, colors[5], (20, 20, 500, 500))

    index = 1  # skip light grey
    for row in range(2):
        for column in range(4):
            pygame.draw.rect(screen, colors[index], ((60 * column) + 20, (60 * row) + 530, 60, 60))
            index += 1

    # Draw clear button
    pygame.draw.rect(screen, colors[5], (280, 530, 120, 55))
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render('Clear', True, colors[0])
    screen.blit(text_surface, (295, 540))

    # Draw sizing buttons
    offset = 0
    sizes = ['1', '2', '3']
    for i in range(3):
        if i > 0:
            offset = 5 * i
        pygame.draw.rect(screen, colors[5], ((36 * i) + 280 + offset, 595, 36, 36))
        text_surface = font.render(sizes[i], True, colors[0])
        screen.blit(text_surface, ((36 * i) + 288 + offset, 598))


def fill_square(screen, color, column, row):
    pygame.draw.rect(screen, color, (20 + (5 * column), 20 + (5 * row), 5, 5))
    pygame.display.update()


def clear_canvas(screen):
    pygame.draw.rect(screen, (255, 255, 255), (20, 20, 500, 500))