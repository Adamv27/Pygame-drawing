import math
import draw
import pygame

pygame.init()
screen = pygame.display.set_mode((540, 720))


class Settings:
    def __init__(self):
        # light grey - black - red - orange - yellow - white - green - blue - purple
        self.colors = [(192, 192, 192), (0, 0, 0), (255, 0, 0),
                       (255, 128, 0), (255, 255, 0), (255, 255, 255),
                       (0, 255, 0), (0, 0, 255), (127, 0, 255)]

        self.current_color = self.colors[1]  # Default color black
        self.size = 1   # Default size 1
        self.size_areas = self.get_size_areas()

    def get_size_areas(self):
        areas = []
        offset = 0
        starting_x_pos = 280
        y_pos = 595
        for i in range(3):
            if i > 0:
                offset = 5 * i
            areas.append(pygame.Rect(((36 * i) + starting_x_pos + offset, y_pos, 36, 36)))
        return areas

    def change_size(self, size):
        self.size = size


def on_color_selector(event_pos: tuple) -> bool:
    in_x_bounds = 20 < event_pos[0] < 260
    in_y_bounds = 530 < event_pos[1] < 650
    return in_x_bounds and in_y_bounds


def on_canvas(event_pos: tuple) -> bool:
    in_x_bounds = 20 < event_pos[0] < 520
    in_y_bounds = 20 < event_pos[1] < 520
    return in_x_bounds and in_y_bounds


def on_clear(event_pos: tuple) -> bool:
    in_x_bounds = 280 < event_pos[0] < 400
    in_y_bounds = 530 < event_pos[1] < 585
    return in_x_bounds and in_y_bounds


def get_color_index(event_pos: tuple) -> int:
    color_column = math.floor((event_pos[0] - 20) / 60)
    color_row = math.floor((event_pos[1] - 530) / 60)
    color_index = color_column if color_row == 0 else 4 + color_column
    return color_index + 1


def drawing(color: tuple):
    mouse_down = True
    while mouse_down:
        for sub_event in pygame.event.get():
            # Mouse button was released and user is no longer
            # In the drawing process
            if sub_event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Mouse position is inside the canvas
        if on_canvas((mouse_x, mouse_y)):
            grid_column = math.floor((mouse_x - 20) / 5)
            grid_row = math.floor((mouse_y - 20) / 5)
            draw.fill_square(screen, color, grid_column, grid_row)

            if settings.size > 1:
                for i in range(settings.size - 1):
                    for pos in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        pos[0] *= i + 1
                        pos[1] *= i + 1
                        draw.fill_square(screen, color, grid_column + pos[0], grid_row + pos[1])
    return


def on_size(event_pos: tuple) -> bool:
    for index, area in enumerate(settings.size_areas):
        if area.collidepoint(event_pos):
            # Index of areas are in order of size
            # Index + 1 = size option
            settings.change_size(index + 1)
            return True


settings = Settings()
draw.draw_canvas(screen, settings.colors)
while True:
    for event in pygame.event.get():
        # Red X is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        # Mouse down could be an attempt to draw or change colors
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left click only
            if event.button == 1:
                if on_canvas(event.pos):
                    drawing(settings.current_color)

                elif on_color_selector(event.pos):
                    settings.current_color = settings.colors[get_color_index(event.pos)]

                elif on_clear(event.pos):
                    draw.clear_canvas(screen)

                elif on_size(event.pos):
                    print(f'New size is {settings.size}')

    pygame.display.update()
