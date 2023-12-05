import sudoku_generator
import pygame, sys
import board

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

        cell_width = self.screen.width // 9
        cell_height = self.screen.height // 10

        cell_surface = pygame.Surface((cell_width, cell_height))
        cell_surface.fill((255, 255, 255))

        text_color = (0, 0, 0)
        text_size = 50
        text_value = ""

        if self.selected:
            pygame.draw.rect(cell_surface, (255, 0, 0), [0, 0][cell_width, cell_height], width=1)

        cell_surface = pygame.Surface((self.col * cell_width, self.row * cell_height),
                                      ((self.col + 1)* cell_width, (self.row + 1) * cell_height))

        if self.original_value != 0:
            # display the original value
            text_value = self.original_value
        elif self.value != 0:
            text_value = self.value
            text_color = (128, 128, 128)
        elif self.sketched_value != 0:
            text_value = self.sketched_value
            text_size = 25

        text_render = pygame.font.Font.render(text_value, color=text_color, size=text_size)
        cell_surface.blit(text_render, ((cell_width // 2) - (text_size // 2),
                                        (cell_height // 2) - (text_size // 2)))
        self.screen.blit(cell_surface, ((self.col * cell_width), (self.row * cell_height)))
