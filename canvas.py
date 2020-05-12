import math
import draw
import pygame

pygame.init()
screen = pygame.display.set_mode((540, 720))


<<<<<<< HEAD
def get_color_areas() -> list:
    # Creates an area for each color in the color selector to
    # check if a color was clicked on
    color_areas = []
    for row in range(2):
        for column in range(4):
            color_areas.append(pygame.Rect(((60 * column) + 20, (60 * row) + 530, 60, 60)))
    return color_areas


def on_color_selector(event_pos) -> bool:
    # Click location (x,y) is within the color selector
    in_x_bounds = 20 < event_pos[0] < 250
=======
def on_color_selector(event_pos: tuple) -> bool:
    in_x_bounds = 20 < event_pos[0] < 260
>>>>>>> development
    in_y_bounds = 530 < event_pos[1] < 650
    return in_x_bounds and in_y_bounds


<<<<<<< HEAD
def on_canvas(event_pos) -> bool:
    # Click location (x,y) is within the white canvas
=======
def on_canvas(event_pos: tuple) -> bool:
>>>>>>> development
    in_x_bounds = 20 < event_pos[0] < 520
    in_y_bounds = 20 < event_pos[1] < 520
    return in_x_bounds and in_y_bounds


<<<<<<< HEAD
def get_color_index(event_pos) -> int:
=======
def on_clear(event_pos: tuple) -> bool:
    in_x_bounds = 280 < event_pos[0] < 400
    in_y_bounds = 530 < event_pos[1] < 585
    return in_x_bounds and in_y_bounds

def get_color_index(event_pos: tuple) -> int:
>>>>>>> development
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
    return


# light grey - black - red - orange - yellow - white - green - blue - purple
colors = [(192, 192, 192), (0, 0, 0), (255, 0, 0),
          (255, 128, 0), (255, 255, 0), (255, 255, 255),
          (0, 255, 0), (0, 0, 255), (127, 0, 255)]

current_color = colors[1]  # Default drawing color - black
draw.draw_canvas(screen, colors)
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
                    drawing(current_color)

                elif on_color_selector(event.pos):
                    current_color = colors[get_color_index(event.pos)]

                elif on_clear(event.pos):
                    draw.clear_canvas(screen)

    pygame.display.update()
