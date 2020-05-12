import math
import draw
import pygame

pygame.init()
screen = pygame.display.set_mode((540, 720))

class Canvas:
    def __init__(self):
        self.rows = 100
        self.columns = 100
        # 100 x 100 grid to draw on
        # Each canvas 'pixel' being 5 pixels length and width
        self.grid = [[0] * self.columns for i in range(self.rows)]
        self.areas = self.get_areas

    @property
    def get_areas(self) -> list:
        # Creates a pygame area for each item in the array to
        # later check if the mouse hovers over it
        areas = []
        for row in range(self.rows):
            for column in range(self.columns):
                areas.append(pygame.Rect(20 + (5 * row), 20 + (5 * column), 5, 5))
        return areas


def get_color_areas() -> list:
    # Creates an area for each color in the color selector to
    # check if a color was clicked on
    color_areas = []
    for row in range(2):
        for column in range(4):
            color_areas.append(pygame.Rect(((60 * column) + 20, (60 * row) + 530, 60, 60)))
    return color_areas


def click_on_color(event_pos) -> bool:
    # Click location was on one of the colored boxes
     color_areas = get_color_areas()
     for area in color_areas:
         if area.collidepoint(event_pos):
             return True


def click_on_canvas(event_pos) -> bool:
    # Each area is an index in a 2d array
    for area in canvas.areas:
        if area.collidepoint(event_pos):
            return True


def get_color_index(event_pos) -> int:
    color_column = math.floor((event_pos[0] - 20) / 60)
    color_row = math.floor((event_pos[1] - 530) / 60)
    color_index = color_column if color_row == 0 else 4 + color_column
    return color_index + 1


def drawing(color):
    mouse_down = True
    while mouse_down:
        for event in pygame.event.get():
            # Mouse button was released and user is no longer
            # In the drawing process
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Mouse position is inside the canvas
        if (20 < mouse_x < 520) and (20 < mouse_y < 520):
            grid_column = math.floor((mouse_x - 20) / 5)
            grid_row = math.floor((mouse_y - 20) / 5)
            draw.fill_square(screen, color, grid_column, grid_row)
    return


# light grey - black - red - orange - yellow - white - green - blue - purple
colors = [(192, 192, 192), (0, 0, 0), (255, 0, 0),
          (255, 128, 0),  (255, 255, 0),  (255, 255, 255),
          (0, 255, 0),  (0, 0, 255),  (127, 0, 255)]

current_color = colors[1]  # Default drawing color - black
canvas = Canvas()

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
                if click_on_canvas(event.pos):
                    drawing(current_color)

                elif click_on_color(event.pos):
                    current_color = colors[get_color_index(event.pos)]

    pygame.display.update()


