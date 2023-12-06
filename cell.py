import sudoku_generator
import pygame, sys

class Cell:

    def __init__(self, value, row, col, screen):
        self.original_value = value
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False



    def set_cell_value(self, value):
        # setter for this cell’s value

        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value

        self.sketched_value = value

    def set_selected(self, is_selected):
        self.selected = is_selected

    def draw(self):
        pygame.draw.rect
        # draws this cell, along with the value inside it.
        # if this cell has a nonzero value, that value is displayed.
        # otherwise, no value is displayed in the cell.
        # the cell is outlined red if it is currently selected.
        # draw the cell
        # current cell is outlined red

        cell_width = self.screen.get_width() // 9
        cell_height = self.screen.get_height() // 10

        cell_surface = pygame.Surface((cell_width - 6, cell_height - 6))
        cell_surface.fill((255, 255, 255))

        text_color = (0, 0, 0)
        text_size = 75
        text_value = ""

        if self.selected:
            pygame.draw.rect(cell_surface, (255, 0, 0), [[0, 0], [cell_width - 6, cell_height - 6]], width=3)


        if self.original_value != 0:
            # display the original value
            text_value = str(self.original_value)
        elif self.value != 0:
            text_value = str(self.value)
            text_color = (128, 128, 128)
        elif self.sketched_value != 0:
            text_color = (128, 128, 128)
            text_value = str(self.sketched_value)
            text_size = 50

        cell_font = pygame.font.Font(None, text_size)
        text_render = cell_font.render(text_value, 0, text_color)
        text_rect = text_render.get_rect(center=(cell_width // 2, cell_height // 2))
        cell_surface.blit(text_render, text_rect)
        self.screen.blit(cell_surface, ((self.col * cell_width) + 3, (self.row * cell_height) + 3))
